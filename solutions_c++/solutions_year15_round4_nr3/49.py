#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

const int N = 8000, M = 30000;
int par[N], first[N], nxt[2*M], ep[2*M], m;
int flo[2*M], cap[2*M];
void init() { m = 0; memset(first,-1,sizeof first); memset(flo,0,sizeof flo); }
void add_edge(int a, int b, int c=1) {
  nxt[m] = first[ep[m]=a], first[ep[m]] = m, cap[m] = c, ++m;
  nxt[m] = first[ep[m]=b], first[ep[m]] = m, cap[m] = 0, ++m; }

int mf_update(int s, int t) {
  int df[N]; memset(df, 0, sizeof df); memset(par, -1, sizeof par);
  queue<int> q; q.push(s); par[s] = -2; df[s] = INF;
  while (!q.empty()) { int cf; int u = q.front(); q.pop();
    for (int v, e = first[u]; e != -1; e = nxt[e])
      if (par[v=ep[e^1]] == -1 && (cf = cap[e]-flo[e]) > 0)
        q.push(v), par[v] = e, df[v] = min(df[u], cf); }
  if (par[t] == -1) return 0;
  for (int e, i = t; i != s; i = ep[e])
    e = par[i], flo[e] += df[t], flo[e^1] -= df[t];
  return df[t]; }

int T, n;
string line, word;
map<string,int> wordID;
vector<int> sent[200];

int main()
{
    ios::sync_with_stdio(0);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        wordID.clear();
        cin >> n;
        getline(cin, line);
        for (int i = 0; i < n; ++i)
        {
            sent[i].clear();
            getline(cin, line);
            stringstream ss(line);
            while (ss >> word)
            {
                if (wordID.find(word) == wordID.end())
                {
                    int id = wordID.size();
                    wordID[word] = id;
                }
                sent[i].push_back(wordID[word]);
            }
        }
        init();
        int S = 7998, T = 7999, indepset = 0;
        for (int i = 0; i < wordID.size(); ++i)
        {
            if (find(sent[0].begin(), sent[0].end(), i) == sent[0].end())
                add_edge(S, 2*i), ++indepset;
            if (find(sent[1].begin(), sent[1].end(), i) == sent[1].end())
                add_edge(2*i+1, T), ++indepset;
        }
        for (int i = 2; i < n; ++i)
        {
            for (int j = 0; j < sent[i].size(); ++j)
            for (int k = 0; k < sent[i].size(); ++k)
                add_edge(2*sent[i][j], 2*sent[i][k]+1);
        }
        while (int df = mf_update(S, T))
            indepset -= df;
        cout << "Case #" << z << ": " << (wordID.size() - indepset) << endl;
    }
}
