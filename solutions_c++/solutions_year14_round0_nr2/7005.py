#include<stdio.h>
#include<string.h>
int T;
int t;
double C,F,X;
double CookieForSec;
int FarmCount;
double time;
double finaltime;
double ans;

int main()
{
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		CookieForSec = 2.0;
		FarmCount = 0;
		time = 0;
		scanf("%lf %lf %lf",&C, &F, &X);		
			ans =(double) (X/CookieForSec);		
			while(1){
				time = time + (double)(C/CookieForSec);
				FarmCount++;
				CookieForSec = CookieForSec + F;
				finaltime = time + (double)(X/CookieForSec);
				if(ans <= finaltime){			
					break;
				}else{
					ans = finaltime;
				}			
			}		
			printf("Case #%d: %.7lf\n",t,ans);		
	}
}