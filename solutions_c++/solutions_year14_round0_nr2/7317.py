#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const double eps=1e-8;
double c,f,x;
int dcmp(double x)
{
	if(fabs(x)<eps) return 0;
	else return x<0?-1:1;
}
int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,kase=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",kase++);
		scanf("%lf%lf%lf",&c,&f,&x);
		double k=x/c-2.0/f;
		if(dcmp(k)<=0)
		{
			printf("%.7f\n",x/2.0);
			continue;
		}
		int b=floor(k);
		double ans1=0,ans2;
		for(int i=0;i<=b;i++) ans1+=c/(2.0+i*f);
		ans1+=x/(2.0+(b+1)*f);
		ans2=ans1+(f*x-(2.0+(b+1)*f)*c)/(2+b*f)/(2+(b+1)*f);
		double ans=min(ans1,ans2);
		//cout<<ans1<<" "<<ans2<<endl;
		printf("%.7f\n",ans);
	}
	return 0;
}
