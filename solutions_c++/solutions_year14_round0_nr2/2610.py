#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
#include<conio.h>

#define MOD 1000000007


using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

    int t;
	double c,f,x;
	scanf("%d",&t);

	for(int test=1;test<=t;test++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		
		double ans=0;
		double rate=2;
		
		while(1)
		{
			double a=c/rate+x/(rate+f);
			double b=x/rate;

			if(a<b)
			{
				ans+=c/rate;
				rate+=f;
			}
			
			else
			{
				ans+=x/rate;
				break;
			}
		}

		printf("Case #%d: %.7f\n",test,ans);
	}

    return 0;
}
