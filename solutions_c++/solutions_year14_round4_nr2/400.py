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

LL a[1024];
int main() {
  int t,n;
  scanf("%d",&t);
  while(t--) {
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
      scanf("%lld",&a[i]);
      a[i] = (LL)INF + (LL)INF - a[i];
      a[i] = llabs(a[i]);
    }
    int ans = 0;
    for(int i=0;i<n;i++) {
      int c1 = 0, c2 = 0;
      for(int j=0;j<i;j++)
        if(a[i] > llabs(a[j]))
          c1++;
      for(int j=i+1;j<n;j++)
        if(a[i] > a[j])
          c2++;
      if(c1 < c2) {
        a[i] = -a[i];
      }
      for(int j=0;j<i;j++)
        if(a[j] > a[i])
          ans++;
    }
    int static kase = 1;
    printf("Case #%d: %d\n",kase++, ans);
  }
  return 0;
}
