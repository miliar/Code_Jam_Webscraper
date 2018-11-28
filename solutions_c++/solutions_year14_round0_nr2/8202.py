#include <iostream>
#include <cstdio>
#include <map>
using namespace std ;
int main()
{
	freopen("D:\\B-large.in","r",stdin) ;
	freopen("D:\\B-large.out","w",stdout) ;
	double p,c,f,x ;
	int t ;
	scanf("%d",&t) ;
	for(int cas=1 ;cas<=t ;cas++)
	{
		scanf("%lf%lf%lf",&c,&f,&x) ;
		p=2.0 ;
		double temp ;
		double ans=x/p ;
		temp=0 ;
		int cnt=0 ;
		while(1)
		{
			double t1=c/p+x/(p+f) ;
			//printf("%lf %lf!!\n",ans,t1) ;
			//if(cnt++>4)break ;
			if(ans<t1+temp)break ;
			else ans=t1+temp ;
			temp+=c/p ;
			p+=f ;
		}
		printf("Case #%d: ",cas) ;
		printf("%.7lf\n",ans) ;
	}
	return 0 ;
} 