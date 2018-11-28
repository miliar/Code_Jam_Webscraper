
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
#include <ctime>
#include <limits.h>
using namespace std;

typedef long long ll;
const double pi=acos (-1.0);
const double eps=1e-9 ;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf=0x3f3f3f3f ;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
#define FILL(a,b) memset(a, b, sizeof(a))
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define snuke(c,itr) for( __typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP make_pair
#define fi first
#define se second
typedef pair <int, int> PII;

int n,k;
int a[10003];
void work() {
	cin>>n>>k;
	int i,j;
	rep(i,n) {
		scanf("%d",a+i);
	}
	sort(a,a+n);

	int ans = 0;

	int l = 0,r = n - 1;
	while (l <= r) {
		if (l == r) {
			ans ++;break;
		}
		else {
			if (a[l] + a[r] <= k) {
				l ++;
				r --;
				ans ++;
			}
			else {
				r --;
				ans ++;
			}
		}
	}
	printf("%d\n",ans);
}

int main ()
{
#ifdef LOCAL
     freopen("in.txt" ,"r", stdin);
      freopen ("out.txt","w",stdout);
#endif
     int t;
     cin>>t;
     int cas = 1;
     while(t--) {
    	 printf("Case #%d: ",cas++);
    	 work();
     }


     return 0 ;
}



