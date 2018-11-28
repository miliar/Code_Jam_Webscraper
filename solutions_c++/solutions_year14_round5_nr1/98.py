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

LL t, n, p, q, r, s;
LL trans[1<<20];
int main() {
  scanf("%lld",&t);
  while(t--) {
    scanf("%lld%lld%lld%lld%lld",&n,&p,&q,&r,&s);
    LL total = 0;
    for(LL i=0;i<n;i++) {
      trans[i] = ((i*p+q)%r) + s;
      total += trans[i];
    }
    LL best = total;
    int p2 = 0;
    LL mid = 0;
    LL left = 0;
    for(int i=0;i<n;i++) {
      LL rem = total - (mid+left); 
      while(mid < rem) {
        best = min(best, max(left, max(mid, rem)));
        best = min(best, max(left, max(mid+trans[p2], rem-trans[p2])));
        mid += trans[p2];
        rem -= trans[p2];
        p2++;
      }
      if(mid >= rem) {
        p2--;
        mid -= trans[p2];
        rem += trans[p2];
      }
      left += trans[i];
      if(mid) {
        mid -= trans[i];
      }
    }
    double ans = ((double)(total-best))/((double)(total));
    int static kase = 1;
    printf("Case #%d: %.10lf\n",kase++, ans);
  }
  return 0;
}
