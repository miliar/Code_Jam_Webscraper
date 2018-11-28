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
int t, n, s, sz[1<<20], used[1<<20];
int main() {
  scanf("%d",&t);
  while(t--) {
    scanf("%d%d",&n,&s);
    for(int i=0;i<n;i++) {
      scanf("%d",&sz[i]);
      used[i] = 0;
    }
    sort(sz, sz+n);
    int p = n-1;
    int ans = 0;
    for(int i=0;i<n;i++) {
      if(used[i]) continue;
      ans++;
      while(p > i) {
        if(sz[i] + sz[p] <= s) {
          used[p] = 1;
          used[i] = 1;
          p--;
          break;
        } else {
          p--;
        }
      }
    }
    int static test = 1;
    printf("Case #%d: %d\n",test++,ans);
  }
  return 0;
}
