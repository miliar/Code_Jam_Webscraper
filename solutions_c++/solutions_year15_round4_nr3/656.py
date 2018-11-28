//ITNOG
#include<bits/stdc++.h>

using namespace std;

//#define int long long
#define rep(i, s, e) for(int i = s; i < e; i ++)
typedef long double ld;

const int maxN = 200+5;
const int mod = 1000*1000*1000 + 7;
const int maxM = 400000;

/*
int head[maxN], mark[maxN];
int source, sink, cnt;
int to[maxM], nxt[maxM], cap[maxM];

void add_edge(int v, int u, int c)
{
    to[cnt] = u; nxt[cnt] = head[v]; cap[cnt] = c; head[v] = cnt ++;
    to[cnt] = v; nxt[cnt] = head[u]; cap[cnt] = 0; head[u] = cnt ++;
}

int dfs(int v, int flow)
{
    mark[v] = 1;
    if(v == sink) return flow;

    for(int e = head[v]; e != -1; e = nxt[e])
    {
	  if(mark[to[e]] || cap[e] == 0) continue;

//	  cout << v << ' ' << to[e] << endl;

	  int ret = dfs(to[e], min(flow, cap[e]));
	  
	  if(ret)
	  {
		cap[e ^ 0] -= ret;
		cap[e ^ 1] += ret;

//		cout << v << ' ' << to[e] << endl;
		return ret;
	  }
    }

    return 0;
}

int get_max_flow()
{
    int flow = 0;
    for(int tmp; (tmp = dfs(source, mod)); flow += tmp)
	  memset(mark, 0, sizeof mark);
    return flow;
}
*/

vector<long long> a[205];

long long has(string s)
{
    long long hs = 0;
    rep(i,0,s.size()) hs = hs * 701 + s[i];
    return hs;
}

bitset<10000> bi[22];

void solve()
{
//    memset(head,-1,sizeof head); cnt = 0;
    int n; cin >> n; cin.ignore();
    vector<long long> tot;
    rep(i,0,n) 
    {
	  string s;
	  getline(cin, s);
	  s += ' '; string res;
	  rep(j,0,s.size())
	  {
		if(s[j] == ' ') { a[i].push_back(has(res)); tot.push_back(has(res)); res = ""; }
		else res += s[j];
	  }
    }
    
    sort(tot.begin(), tot.end()); tot.resize(unique(tot.begin(), tot.end()) - tot.begin());
    rep(i,0,n) sort(a[i].begin(), a[i].end()), a[i].resize(unique(a[i].begin(), a[i].end()) - a[i].begin());
    
    rep(i,0,n)
    {
	  rep(j,0,a[i].size())
	  {
		int ps = lower_bound(tot.begin(), tot.end(), a[i][j]) - tot.begin();
		bi[i][ps] = 1;
	  }
    }

//    rep(i,0,n) cout << bi[i] << ' '; cout << endl;

    int answer = mod;
    rep(mask,0,(1<<n))
    {
//	  cout << mask << endl;
	  if(mask >> 0 & 1) continue;
	  if(!(mask >> 1 & 1)) continue;
	  bitset<10000> c1,c2;
	  rep(i,0,n) if(mask >> i & 1) c1 |= bi[i];
	  else c2 |= bi[i];
	  
	  c1 &= c2; int ans = c1.count();

	  answer = min(answer, ans);
    }

    rep(i,0,n) a[i].clear();
    memset(bi,0,sizeof bi);
    cout << answer << endl;
}


main()
{
//    ios::sync_with_stdio(0); cin.tie();
    int T; cin >> T;
    rep(i,1,T+1)
    {
	  printf("Case #%d: ", i);
	  solve();
    }
    return 0;
}
