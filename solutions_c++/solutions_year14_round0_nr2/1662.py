#include <cstdio>
using namespace std;
int T,ll;
double C,F,X,ans,s,pro;
void work()
{
	ll++;
  	scanf("%lf %lf %lf",&C,&F,&X);
  	ans=1e9;s=0;pro=2;
	while (ans>s+X/pro) ans=s+X/pro,s+=C/pro,pro+=F;
  	printf("Case #%d: %.7lf\n",ll,ans);
}
int main()
{
	freopen ("a.in","r",stdin);
	freopen ("a.out","w",stdout);
	int T;
  	scanf("%d",&T);
  	while (T) T--,work();
  	return 0;
}
