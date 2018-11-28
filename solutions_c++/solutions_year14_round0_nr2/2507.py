#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
using namespace std;
typedef long long int ll;
#define inf 1000000007
#define iit(n) scanf("%lld",&n)
#define oit(n) printf("%lld",n)
#define pb(n) push_back(n)
#define REP(i,j,n) for(i=j;i<n;i++)
#define READ(x) freopen(x, "r", stdin)
#define WRITE(x) freopen(x, "w", stdout)
#define mp make_pair
int main()
{
//  ios_base::sync_with_stdio(0);cin.tie(0);
	READ("inp");
	WRITE("out.txt");
	int tc;
	cin>>tc;
	int cas;
	for(cas=1;cas<=tc;cas++) {
		double c,f,x;
		cin>>c>>f>>x;
		double rate=2.0;
		double time=0;
		double exp;
		double t,r,ans;
//		int iter=10;
		while(1) {
			exp=(x/rate);
			t=(c/rate);
			r=rate+f;
			if(time+exp<(time+t+(x/r))){
				ans=time+exp;
				break;
			}
			time+=t;
			rate+=f;
//			cout<<time<<" "<<exp<<" "<<t<<" "<<r<<" "<<(x/r)<<"\n";
		}
		printf("Case #%d: %.7lf\n",cas,ans);
	}
	return 0;
}

