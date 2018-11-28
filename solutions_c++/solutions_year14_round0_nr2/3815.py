#include <bits/stdc++.h>
#define fi "B.INP"
#define fo "B.OUT"
#define nmax
#define INF
using namespace std;
typedef double dd;
//VARIABLES
int test;
dd x,y,S,m,n,res;
//PROTOTYPES
void Process();

//MAIN
int main()
{
	int tc;
	freopen(fi,"r",stdin);
	freopen(fo,"w",stdout);
	scanf("%d",&tc);
	while (tc--) Process();
	return 0;
}

//FUNCTIONS
void Process()
{
	scanf("%lf%lf%lf",&x,&y,&S);
	m=0.0;n=2.0;res=S/n;
	while (true)
	{
		m+=x/n;
		n+=y;
		if (res<m+S/n) break;
		res=m+S/n;
	}
	printf("Case #%d: %.7lf\n",++test,res);
}
