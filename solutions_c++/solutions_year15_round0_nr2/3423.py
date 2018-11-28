/* Author : RISHAV GOYAL */

#include <bits/stdc++.h>
using namespace std;

#define LL long long int
#define UL unsigned long long int

#define imax INT_MAX
#define imin INT_MIN
#define LLmax LLONG_MAX
#define LLmin LLONG_MIN

#define FOR(i,a,b) for(int i= (int)a; i<= (int)b; i++)
#define rep(i,n) for(int i= int(1); i<= (int)n; i++)
#define FORd(i,a,b,d) for(int i=(int)a; i<= (int)b; i+=(int)d)

#define pr() printf("Reached here 1...\n");
#define pr1() printf("Reached here 2...\n");

#define CLR(a) memset(a,0,sizeof(a));
#define SET(a) memset(a,-1,sizeof(a));

#define str strlen
#define pb(x) push_back(x)
#define mp make_pair
#define ii pair<int,int>
#define ll pair<LL,LL>

#define F first
#define S second
#define gcd(a,b) __gcd(a,b)

#define mod int(1e9 + 7)
#define MAX int(1e5 + 10)

#define si(a) scanf("%d",&a);

#define VI vector<int>
#define VL vector<LL>
#define VS vector<string>
#define VC vector<char>

LL powmod(LL a,int b,int n){LL rm=1;while (b){if (b % 2) { rm = (rm * a) % n; }a = (a * a) % n;b /= 2;}return rm;}

int main()
{
	int T,n,p[1010];
	cin >> T;
	rep(ts,T){
		si(n);
		int mx = 0;
		rep(i,n) {
			si(p[i]);
			mx=max(mx,p[i]);
		}
		int ans = 1e9;
		for(int i=1;i<=mx;++i){
			int cost = 0;
			for(int j=1;j<=n;++j){
				cost += (p[j]/i) + !!(p[j]%i) -1;
			}
			cost += i;
			ans = min(ans , cost);
		}
		printf("Case #%d: %d\n",ts,ans);
	}
	return 0;
}

