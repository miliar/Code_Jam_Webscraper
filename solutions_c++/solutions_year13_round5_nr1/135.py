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
#define FOR(i,a,b)  for(Int i=(a);i<=(b);++i)
#define sz(s) (int)(s).size()
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
void assert(bool x){if(!x)throw -1;}
const int inf = 1000000000;
const int MOD = 1000000007;
const double pi = acos(-1.0);

const int N = 1000;
Int x[N+1];

double solve() {
	Int B;cin>>B;
	int n;cin>>n;
	FOR(i,1,n) cin>>x[i];
	while(n<37){
		++n;
		x[n]=0;
	}
	x[0]=0;
	sort(x,x+n+1);

	double ans = 0;
	FOR(i,2,n) {
		Int now=0;
		FOR(j,1,i-1)now+=x[i-1]-x[j];
		if(now>B)break;
		Int add = B-now;
		Int h1 = add/(i-1);
		h1=min(h1,x[i]-x[i-1]-1);

		FOR(h,max(h1-5,0LL),h1)
		{
			vector<Int> w;
			FOR(j,1,i-1)w.pb(x[i-1]-x[j]+h);
			sort(w.begin(),w.end(),greater<Int>());

			Int waste = h*Int(i-1) + now;
			Int bad=0;
			Int lose=0;
			while(waste+bad<=B && sz(w)>=1) {
				double score=(waste-lose)*36.0/sz(w) - waste-bad;
				ans=max(ans,score);
				++bad;
				lose+=w.back();
				w.pop_back();
			}
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","wb",stdout);	
	int tests;
	scanf("%d\n",&tests);
	for(int test_id=1;test_id<=tests;++test_id) {
		double ans = solve();
		cout<<"Case #"<<test_id<<": ";
		printf("%.9lf\n",ans);
	}
}  