#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdio>
#include<string.h>
#include<set>
#include<map>
#include<time.h>
using namespace std;

typedef long long Int;
#define FOR(i,a,b)  for(int i=(a);i<=(b);++i)
#define sz(s) (int)(s).size()
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
void assert(bool x){if(!x)throw -1;}
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi = acos(-1.0);

double dp[1<<20];

double solve() {
	string s;
	cin>>s;
	int n=sz(s);
	for(int mask=(1<<n)-1;mask>=0;--mask) {
		if(mask==(1<<n)-1)dp[mask]=0;else {
			dp[mask]=0;
			for(int i=0; i<n; ++i){
				int cur=n;
				int j=i;
				while(mask&(1<<j)) {
					j=(j+1)%n;
					--cur;
				}
				dp[mask]+=(dp[mask^(1<<j)]+cur)/double(n);
			}
		}
	}

	int mask=0;
	FOR(i,0,sz(s)-1)if(s[i]=='X')mask+=(1<<i);
	return dp[mask];
}

int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","wb",stdout);	
	int tests;
	scanf("%d\n",&tests);
	for(int test_id=1;test_id<=tests;++test_id) {
		double ans = solve();
		cout<<"Case #"<<test_id<<": ";
		printf("%.10lf\n",ans);
	}
}  