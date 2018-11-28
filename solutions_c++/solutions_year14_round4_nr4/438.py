/*==================================================*\
 | Author: ziki
 | Created Time: 
 | File Name: 
 | Description: 
\*==================================================*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
 
using namespace std;
using namespace rel_ops;
 
typedef long long int64;
typedef long long ll;
typedef unsigned long long uint64;
typedef unsigned long long ull;
const double pi=acos(-1.0);
const double eps=1e-11;
const int inf=0x7FFFFFFF;
template<class T> inline bool checkmin(T &a,T b){return b<a?a=b,1:0;}
template<class T> inline bool checkmax(T &a,T b){return b>a?a=b,1:0;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define mem(a,b) memset(a, b, sizeof(a))
#define clr(a) memset(a, 0, sizeof(a))
#define rep(i,n) for(int i=0; i<int(n); i++)
#define repit(i,v) for(typeof(v.begin()) i=v.begin(); i!=v.end(); i++)
#define iter(v) typeof(v.begin())
#define ff first
#define ss second
#define sz(x) int(x.size())
#ifdef LOCAL
#define dbg(args...) printf(args); //##__VA_ARGS__
#define dout cout
#define out(x) (cout<<#x<<": "<<x<<endl)
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}
#else
#define dbg(...)
#define dout if(true);else cout
#define out(...)
#define show(...)
#endif


const int SIGMA_SIZE = 33;
const int MAXNODE = 11000;
const int MAXS = 150 + 10;

struct AhoCorasickAutomata {
  int ch[MAXNODE][SIGMA_SIZE];
  int f[MAXNODE];    // fail函数
  int val[MAXNODE];  // 每个字符串的结尾结点都有一个非0的val
  int last[MAXNODE]; // 输出链表的下一个结点
  int cnt[MAXS];
  int sz;

  void init() {
    sz = 1;
    memset(ch[0], 0, sizeof(ch[0]));
    memset(cnt, 0, sizeof(cnt));
  }

  // 字符c的编号
  int idx(char c) {
      return c - 'A';
  }

  // 插入字符串。v必须非0
  int insert(char *s, int v) {
    int u = 0, n = strlen(s);
    for(int i = 0; i < n; i++) {
      int c = idx(s[i]);
      if(!ch[u][c]) {
        memset(ch[sz], 0, sizeof(ch[sz]));
        val[sz] = 0;
        ch[u][c] = sz++;
      }
      u = ch[u][c];
    }
    val[u] = v;
    return u;
  }

  // 计算fail函数
  void getFail() {
    queue<int> q;
    f[0] = 0;
    // 初始化队列
    for(int c = 0; c < SIGMA_SIZE; c++) {
      int u = ch[0][c];
      if(u) { f[u] = 0; q.push(u); last[u] = 0; }
    }
    // 按BFS顺序计算fail
    while(!q.empty()) {
      int r = q.front(); q.pop();
      for(int c = 0; c < SIGMA_SIZE; c++) {
        int u = ch[r][c];
        if(!u) {ch[r][c] = ch[f[r]][c]; continue;}
        q.push(u);
        int v = f[r];
        f[u] = ch[v][c];
        last[u] = val[f[u]] ? f[u] : last[f[u]];
      }
    }
  }
} ac[5];

int n, m;
int ans, sum;
int p[10];
char ch[100][100];
void dfs(int d) {
    if (d == n) {
        for (int i = 0; i < m; i++) 
            ac[i].init();
        for (int i = 0; i < n; i++) 
            ac[p[i]].insert(ch[i], 0);
        int s = 0;
        rep(i, m) {
            if (ac[i].sz > 1) 
                s += ac[i].sz;
        }
        if (s > ans) {
            ans = s;
            sum = 1;
        }
        else if (ans == s) {
            sum ++;
        }
        return;
    }
    int &k = p[d];
    for(k = 0; k < m; k++) 
        dfs(d+1);

}

int main() {
    int T;
    cin >> T;
    rep(cas, T) {
        scanf("%d%d", &n, &m);
        rep(i, n) scanf("%s", ch[i]);
        ans = -1;
        dfs(0);
        printf("Case #%d: %d %d\n", cas+1, ans, sum);
    }
    return 0;
}
