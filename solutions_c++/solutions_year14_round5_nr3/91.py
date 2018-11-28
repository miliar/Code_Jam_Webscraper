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
#define N 16
int dp[N][1<<N][2*N];
int cou, t, n;
char type[N];
int id[N];

int bits(int mask) {
  int ret = 0;
  for(int i=0;i<cou;i++)
    if((mask>>i)&1)
      ret++;
  return ret;
}

int rec(int loc, int mask, int ext) {
  if(ext < 0 || ext >= 2*N)
    return INF;
  int& ret = dp[loc][mask][ext];
  if(ret == -1) {
    ret = INF;
    if(loc == n) {
      ret = bits(mask) + ext;
    } else {
      if(type[loc] == 'E') {
        if(id[loc] == -1) {
          for(int i=0;i<cou;i++) {
            if(!((mask>>i)&1)) {
              ret = min(rec(loc+1, mask | (1<<i), ext), ret);
            }
          }
          ret = min(rec(loc+1, mask, ext+1), ret);
        } else {
          if((mask>>id[loc])&1) {
            ret = INF;
          } else {
            ret = min(ret, rec(loc+1, mask | (1<<id[loc]), ext));
          }
        }
      } else {
        if(id[loc] == -1) {
          for(int i=0;i<cou;i++) {
            if(((mask>>i)&1)) {
              ret = min(ret, rec(loc+1, mask - (1<<i), ext));
            }
          }
          ret = min(ret, rec(loc+1, mask, ext-1));
        } else {
          if((mask>>id[loc])&1) {
            ret = min(ret, rec(loc+1, mask - (1<<id[loc]), ext));
          } else {
            ret = INF;
          }
        }
      }
    }
  }
  return ret;
}
map < int , int > mapp;
int main() {
  scanf("%d",&t);
  while(t--) {
    scanf("%d",&n);
    cou = 0;
    mapp.clear();
    mapp[0] = -1;
    for(int i=0;i<n;i++) {
      scanf(" %c %d",&type[i], &id[i]);
      if(mapp.find(id[i])==mapp.end()){
        mapp[id[i]] = cou++;
      }
      id[i] = mapp[id[i]];
    }
    memset(dp, -1, sizeof(dp));
    int ans = INF;
    for(int mask = 0;mask<(1<<cou);mask++) {
      for(int ext=0;ext<=n;ext++) {
        if(rec(0, mask, ext) <= INF) {
          ans = min(ans, rec(0, mask, ext));
        }
      }
    }
    int static kase = 1;
    if(ans != INF) {
      printf("Case #%d: %d\n",kase++, ans);
    } else {
      printf("Case #%d: CRIME TIME\n",kase++);
    }
  }
  return 0;
}
