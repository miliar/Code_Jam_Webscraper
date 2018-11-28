/*************************************************************************
	> File Name: 2.cpp
	> Author:hyh 
	> Mail: hyhdtcpelo@163.com 
	> Created Time: Sat 12 Apr 2014 11:37:00 AM CST
 ************************************************************************/

#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	double X,C,F;
	int T,k=0;
	FILE *out=fopen("out2.txt","w");
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		double tmp1,tmp2,now=2,money=0,ans=0;
		if(X<=C)
			ans=X/now;
		else
			while(1)
			{
		//		cout<<money<<' '<<now<<endl;
			//	sleep(1);
				if(C>=money)
				{
					ans+=(C-money)/now;
					money=C;
				}
				tmp1=(X-money+C)/(now+F);
				tmp2=(X-money)/now;
				if(tmp1<=tmp2&&tmp2-tmp1>=0.0000001)
				{
					money-=C;
					now+=F;
					continue;
				}
				ans+=tmp2;
				break;
			}
		fprintf(out,"Case #%d: %.7lf\n",++k,ans);

	//	printf("Case #%d: %.7lf\n",k,ans);
	}
	fclose(out);
	return 0;
}

