// Author: Xujie Si
// Email: six@gatech.edu
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;

#define FOR(i,X) for(int i=0;i<(X);++i)
#define PB(X) push_back( (X) )


namespace sxj{

  typedef long long LL;
  typedef vector<int> VI;

  priority_queue<int> maxQ; // largest on the top
  priority_queue<int, VI, greater<int> > minQ; // smallest on the top

  auto cmp1 = [](int& a, int& b) -> bool {return a>b;};
  auto dbg = ostream_iterator<int>(cerr, ",");



  // the maximum number of vertices
  const int N = 4400;
  const int NN = N + 10;

  const int E=1000000+10; 
  const LL oo=1LL<<20; 
  const LL MOD=10000LL;

  // adjacency matrix (fill this up)
  // If you fill adj[][] yourself, make sure to include both u->v and v->u.
  LL cap[NN][NN], deg[NN], adj[NN][NN];

  // BFS stuff
  int q[NN], prev[NN];

  LL dinic( int n, int s, int t )
  {
    LL flow = 0;

    while( true )
      {
        // find an augmenting path
        memset( prev, -1, sizeof( prev ) );
        int qf = 0, qb = 0;
        prev[q[qb++] = s] = -2;
        while( qb > qf && prev[t] == -1 )
	  for( int u = q[qf++], i = 0, v; i < deg[u]; i++ )
	    if( prev[v = adj[u][i]] == -1 && cap[u][v] )
	      prev[q[qb++] = v] = u;

        // see if we're done
        if( prev[t] == -1 ) break;

        // try finding more paths
        for( int z = 0; z < n; z++ ) 
	  if( cap[z][t] && prev[z] != -1 )
	    {
	      LL bot = cap[z][t];
	      for( int v = z, u = prev[v]; u >= 0; v = u, u = prev[v] ){
		//bot <?= cap[u][v];
		bot = min(bot, cap[u][v]);
	      }
	      if( !bot ) continue;

	      cap[z][t] -= bot;
	      cap[t][z] += bot;
	      for( int v = z, u = prev[v]; u >= 0; v = u, u = prev[v] )
		{
		  cap[u][v] -= bot;
		  cap[v][u] += bot;
		}
	      flow += bot;
	    }
      }

    return flow;
  }



  int common(vector<string>& va, vector<string>& vb){
    set<string> st_1, st_2;
    for(string& x : va) st_1.insert(x);
    for(string& x : vb) st_2.insert(x);

    int res  =0;
    for(const string& x: st_1)
      if(st_2.find(x) != st_2.end()) ++res;
     
    return res;
  }


  //vector<string> vs[NN];
  set<string> st[NN];


  char buf[1<<20];

  void solve(){
    // exact implementation appears here

    int n;
    cin>>n;

    char c;
    c  = getchar();
    while(c!='\n') c = getchar();


   

    for(int i=0;i<n;++i){
      //vs[i].clear();
      st[i].clear();

      gets(buf);
      int len = strlen(buf);
      int j = 0, ct=0;
      string s="";
      while(j<len){
	if(buf[j]==' '){
	  if(s.length() == 0) fprintf(stderr,"empty words, i=%d, j=%d, ct=%d\n", i, j, ct);

	  //vs[i].push_back(s);
	  st[i].insert(s);

	  s = "";
	  ++ct;
	}

	while(buf[j]==' ') ++j;

	s += buf[j];
	++j;
      }

      if(s.length() > 0) st[i].insert(s);//vs[i].push_back(s);
    }

 
   //for(int i=0;i<n;++i) fprintf(stderr,"%d th line has %lu words\n",i, vs[i].size());

    set<string> words;


    map<string, int> mp;

    for(int i=0;i<n;++i){
      for(const string& x : st[i])
	words.insert(x);
    }

    int id = n+2;
    for(const string& x : words){
      mp[x] = id;

      cap[id][n] = cap[n][id] = oo;
      cap[id][n+1] = cap[n+1][id] = oo;

      ++id;
    }
    

    memset( cap, 0, sizeof( cap ) );
    if(N <= n) fprintf(stderr, " N is less than n, N=%d, n=%d\n",N, n);
    int s = n; // english
    int t = n + 1; // french

    for(int i=0;i<n;++i){
      //for(int j=i+1; j< n; ++j){
      //cap[i][j] = cap[j][i] = common(vs[i], vs[j]);
      //}
      
      for(const string& x : words){
	if(st[i].find(x) == st[i].end()) continue;

	int y = mp[x];
	cap[i][y] = cap[y][i] = 1;
      }

      cap[i][n] = cap[n][i] = 0;
      cap[i][n+1] = cap[n+1][i] = 0;
    }


    cap[0][n+1] = cap[n+1][0] = oo;
    cap[1][n] = cap[n][1] = oo;


    for( int u = 0; u < n+2; u++ )
      for( int v = 0; v < n+2; v++ ){
	//fprintf(stderr, "%d -> %d : %lld\n", u, v, cap[u][v]);
      } 


    // init the adjacency list adj[][] from cap[][]
    memset( deg, 0, sizeof( deg ) );
    for( int u = 0; u < id; u++ )
      for( int v = 0; v < id; v++ ) 
	if( cap[u][v] || cap[v][u] )
	  adj[u][deg[u]++] = v;

    cout<< dinic(id, n, n+1) << endl;

  }




} // endof sxj

int main()
{
  int cs = 0, T;
  scanf("%d",&T);
  while(++cs <= T){
    printf("Case #%d: ", cs);
    sxj::solve();
  }
  return 0;
}
