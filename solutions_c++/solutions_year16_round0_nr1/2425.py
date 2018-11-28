
#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi  vector<int>
#define pb  push_back
#define mp  make_pair
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define sci(x) scanf("%d",&x);
#define scl(x) scanf("%lld",&x);
#define scs(x) scanf("%s",x);
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 100000000000000000LL
#define LL long long

const int N = 1e5+5;
int main() {
  freopen("lg1.in","r",stdin);
  freopen("lgo1.out","w",stdout);
  int t;sci(t);
  int cs = 0;
  while(t--) {
    LL num;
    scl(num);
    if(num == 0) {
      printf("Case #%d: INSOMNIA\n",++cs);
      continue;
    }
    int cnt = 0;
    int mask = 0;
    LL beg = num;
    while(1) {
      LL temp = num;
      while(temp) {
	int dig = temp%10;
	mask|=(1<<dig);
	temp/=10;
      }
      if(mask == 1023) {
	 printf("Case #%d: %lld\n",++cs,num);
	break;
      }
      num+=beg;
    }
  }
}
