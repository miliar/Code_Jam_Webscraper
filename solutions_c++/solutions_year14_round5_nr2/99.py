#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >
#define N 101
char vis[N][N*10+1][2][201];
int ans[N][N*10+1][2][201];
int burn = 0;
int t,n, p,q,h[N+10], g[N+10];

int rec(int loc, int fre, int turn, int hel) {
  if(loc == n)
    return 0;
  if(vis[loc][fre][turn][hel] == burn)
    return ans[loc][fre][turn][hel];
  vis[loc][fre][turn][hel] = burn;
  int& ret = ans[loc][fre][turn][hel];
  ret = 0;
  if(turn == 0) {
    ret = max(ret, rec(loc, fre+1, 1 - turn, hel));
    if(hel <= p) {
      ret = max(ret, rec(loc+1, fre, 1 - turn , h[loc+1]) + g[loc]);
    }
    else {
      ret = max(ret, rec(loc, fre, 1 - turn, hel - p));
    }
  } else {
    if(hel <= q) {
      ret = rec(loc+1, fre, 1 - turn, h[loc+1]);
    } else {
      ret = rec(loc, fre, 1 - turn, hel - q);
    }
    if(fre) {
      if(hel <= p) {
        ret = max(ret, rec(loc+1, fre - 1, turn, h[loc+1]) + g[loc]);
      } else {
        ret = max(ret, rec(loc, fre - 1, turn, hel - p));
      }
    }
  }
  return ret;
}

int main() {
  scanf("%d",&t);
  while(t--) {
    burn++;
    scanf("%d%d%d",&p,&q,&n);
    for(int i=0;i<n;i++) {
      scanf("%d%d",&h[i], &g[i]);
    }
    int static kase = 1;
    printf("Case #%d: %d\n",kase++, rec(0,0,0,h[0]));
  }
  return 0;
}
