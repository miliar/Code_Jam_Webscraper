#include <bits/stdc++.h>
#include <sys/time.h>

using namespace std;

#define FI first
#define SE second
#define X first
#define Y second
#define ST first
#define ND second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef vector<int> VI;
typedef long double LD;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

double getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;
}

const int INF = 1000000001;
const int N=5000;
VI kraw[N];
VI::iterator begin[N];
int c[N][N];
int dist[N];

void AddEdge(int a,int b,int cc){
	c[a][b]+=cc;
	kraw[a].PB(b);
	kraw[b].PB(a);
}
int q[N];

int bfs(int s,int t,int n){
	REP(i,n) dist[i]=-1;
	dist[s]=0;
	int beg=0,end=0;
	q[end++]=s;
	while (beg<end){
		int v=q[beg++];
		FORE(it,kraw[v]) if (c[v][*it]>0 && dist[*it]==-1){
			dist[*it]=dist[v]+1;
			q[end++]=*it;
		}
	}	
	return dist[t]!=-1;
}

int dfs(int x,int t,int minimum){
	int res=0;
	if (x==t || minimum==0) return minimum;
	for(VI::iterator &it=begin[x];it!=kraw[x].end(); ++it){
		if (dist[x]+1==dist[*it] && c[x][*it]>0){
			int y=dfs(*it,t,min(minimum,c[x][*it]));
			c[x][*it]-=y;
			c[*it][x]+=y;
			minimum-=y;
			res+=y;
			if (minimum==0) break;
		}
	}
	return res;
}

int Maxflow(int s,int t,int n){
	int res=0;
	while (bfs(s,t,n)){
		REP(i,n) begin[i]=kraw[i].begin();
		res+=dfs(s,t,INF);
	}
	return res;
}

int alg() {
  REP(i,N) kraw[i].clear();
  REP(i,N) REP(j,N) c[i][j]=0;
  int n_sentences;
  map<string, int> words;
  int n_words = 0;
  cin >> n_sentences;
  string s;
  getline(cin, s);
  REP (i, n_sentences) {
      getline(cin, s);
      stringstream ss(s);
      while (!ss.eof()) {
          string t;
          ss >> t;
          if (words.find(t) == words.end()) {
              AddEdge(n_sentences + 2 * n_words, n_sentences + 2 * n_words + 1, 1);
              words[t] = n_words++;
          }
          int x = words[t];
          AddEdge(i, n_sentences + 2 * x, 1);
          AddEdge(n_sentences + 2 * x + 1, i, 1);
      }
  }
  int n = 2 * n_words + n_sentences;
  return Maxflow(0,1,n);
}

int main() {
    int d;
    cin >> d;
    FOR (i, 1, d + 1) {
        cout << "Case #" << i << ": " << alg() << endl;
    }
}

