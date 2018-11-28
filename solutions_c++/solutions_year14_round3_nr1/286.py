#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define   M 1000000007

typedef long long  LL;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

LL gcd(LL a,LL b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

LL modexp(LL a,LL b)
{
	if(b==0) return 1;
	if(b%2) return ((a%M)*modexp(a,b-1))%M;
	LL q=modexp(a,b/2);
	return (q*q)%M;
}

vector<pi> all[15];

void gen(int dep)
{
	int i,j;

	for(i=0;i<all[dep-1].size();i++)
	  for(j=0;j<all[dep-1].size();j++) if(i!=j)
	  {
		  int a= all[dep-1][i].first*all[dep-1][j].second;
		  int b= all[dep-1][i].second*all[dep-1][j].first;
		  b*=2;
		  all[dep].pb(MP(a,b));
		  if(!b || !a) continue;
	  }
	  all[dep].pb(MP(0,1));
	all[dep].pb(MP(1,1));
	for(i=0;i<all[dep].size();i++)
		printf("%d %d/%d\n",dep,all[dep][i].first,all[dep][i].second);
}
int main()
{
	int n,m,i,j,k,tests,cs=0;

	 freopen("D:\\GCJ2\\A-small-attempt0.in","r",stdin);
	 freopen("D:\\GCJ2\\A-small-attempt0.out","w",stdout);

	/*all[0].pb(MP(0,1));
	all[0].pb(MP(1,1));
	
	for(i=1;i<=3;i++)
	{
		gen(i);
	}*/

	scanf("%d",&tests);
	while(tests--)
	{
		 LL p,q;
		 scanf("%lld/%lld",&p,&q);

		 LL g=gcd(p,q);

		 p/=g;
		 q/=g;

		 printf("Case #%d: ",++cs);

		 if( (q&(q-1)))
		 {
			 printf("impossible\n");
			 continue;
		 }

		 int ans=1;

		 while(1)
		 {
			 p*=2;
			 if(p>=q) break;
			 ans++;
		 }

		printf("%d\n",ans);
	}
	return 0;
}