#include <iostream>
#include<algorithm>
#include<cstdio>
#define inf 99999999.000
using namespace std;
double ken[11],na[11];
int fk[11],fn[11];
int main()
{
	int i,j,k,f,n,test,t,war_na,posk,posn,pk,pn,ans,ans2;
	double a,b,c,mina,maxb;
	scanf("%d",&t);
	for(test=1;test<=t;test++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%lf",&na[i]);
		for(i=0;i<n;i++)scanf("%lf",&ken[i]);
		for(i=0;i<n;i++)fk[i]=fn[i]=0;
		f=0;
		sort(ken,ken+n);
		sort(na,na+n);
		ans=0;
		for(i=0;i<n;i++)
		{
			f=0;
			mina=inf;
			maxb=0;
			for(j=0;j<n;j++)
			{
				if(!fk[j])
				{
					if(ken[j]>na[i])
					{
						f=1;
						//printf("%lf,%lf\n",ken[i],na[j]);
						a=ken[j]-na[i];
						if(a<mina)
						{
							mina=a;
							posk=j;
							//posn=i;
						}
					}
					else
					{
						b=na[i]-ken[j];
						//printf("%lf,%lf\n",ken[i],na[j]);
						if(b>maxb)
						{
							maxb=b;
							pk=j;
							//pn=i;
						}
					}
                }
			}
			if(!f)
			{
                fk[pk]=1;
                ans++;
			}
			else fk[posk]=1;
		}
		//printf("%d\n",ans);
		for(i=0;i<n;i++)fk[i]=fn[i]=0;
		ans2=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(!fn[j])
                {
                    if(na[j]>ken[i])
                    {
                        fn[j]=1;
                        ans2++;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",test,ans,ans2);




	}
	return 0;
}
