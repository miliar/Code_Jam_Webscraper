#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
double F,C,X;
int main()
{	
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\B-small-attempt0.in","r",stdin);
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\result.out","w",stdout);
	scanf("%d",&T);
	int ca=0;
	while(T--)
		{		
		ca++;
		scanf("%lf%lf%lf",&C,&F,&X);
		printf("Case #%d: ",ca);
		if(X-2*C/F<0)
			{
			printf("%.7f\n",X/2);
			continue;
			}
		int temp=(int)((X-2*C/F)/C);
		double ans=0;
		for(int i=0;i<temp;i++)
			{
			double tt=i*F;
			ans+=C/(2+tt);
			}
		ans+=X/(2+F*temp);
		printf("%.7f\n",ans);
		}
return 0;

}#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;
int T;
double F,C,X;
int main()
{	
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\B-small-attempt0.in","r",stdin);
	freopen("E:\\ACM  练习\\代码文件\\cao11\\cao11\\result.out","w",stdout);
	scanf("%d",&T);
	int ca=0;
	while(T--)
		{		
		ca++;
		scanf("%lf%lf%lf",&C,&F,&X);
		printf("Case #%d: ",ca);
		if(X-2*C/F<0)
			{
			printf("%.7f\n",X/2);
			continue;
			}
		int temp=(int)((X-2*C/F)/C);
		double ans=0;
		for(int i=0;i<temp;i++)
			{
			double tt=i*F;
			ans+=C/(2+tt);
			}
		ans+=X/(2+F*temp);
		printf("%.7f\n",ans);
		}
return 0;

}