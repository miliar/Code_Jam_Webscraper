#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<stack>
//#include<ctime>

using namespace std;
typedef int LL;
double c,f,x;
double MN(double a,double b){return (a<b)?a:b;}
struct obj
{
	double p;
	obj(){};
	obj(double a){p=a;}
};
stack<obj> S;
int main()
{
	LL t,cas=0,i;
	double ans;
	freopen("B-large.in","r",stdin);
	freopen("out.in","w",stdout);
//	double t1=clock();
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		obj src(2);
		obj top;
		S.push(src);
		ans=0;
		for(i=1;i<=1000000;i++)
		{
			obj Now(S.top().p+f);
			S.push(Now);
		}
		top=S.top();
		S.pop();
		ans=x/top.p;
		while(S.empty()==false)
		{
			top=S.top();
			S.pop();
			ans=MN(x/top.p,c/top.p+ans);
		}
		printf("Case #%d: %.7lf\n",++cas,ans);
	}
//	t1=clock()-t1;
//	printf("%lf\n",t1/CLOCKS_PER_SEC);
	return 0;
}