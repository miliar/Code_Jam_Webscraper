#include <cstdio>
#include <algorithm>

int T;
double c,f,x,ans;

double cal(int n)
{
	if (n<0) n=0;
	double tmp=x/(2+n*f);
	for (int i=0;i<n;++i) tmp+=c/(2+i*f);
	return tmp;
}
int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=std::min(cal(x/c-2/f-1),cal(x/c-2/f));
		printf("Case #%d: %.7f\n",t,ans);
	}
	return 0;
}