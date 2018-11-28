#include <stdio.h>

double p[210] ,p2[210];
double dp[210][210];
int sta[510] ,np;
double max(double aa ,double bb)
{
	if (aa>bb)	
	{
		return aa;
	}
	return bb;
}
int main(void)
{
	int tt ,ii;
	int n ,k ,i ,j ,mi ,iii ,ti;
	double ans ,tempans;
	double pp ,pp2;
	
	scanf("%d" ,&tt);
	for (ii=1 ; ii<=tt ; ii++)
	{
		scanf("%d %d" ,&n ,&k);
		for (i=1 ; i<=n ; i++)
		{
			scanf("%lf" ,&p[i]);
		}
		
		ans=0;
		
		mi=1<<n;
		for (ti=0 ; ti<mi ; ti++)
		{
			np=0;
			iii=ti;	
			j=1;
			while (iii)
			{
				if (iii&1)
				{
					sta[++np]=j;	
				}
				iii>>=1;
				j++;
			}
			if (np==k)
			{
				for (j=1 ; j<=k ; j++)
				{
					p2[j]=p[sta[j]];
				}
		
				dp[0][0]=1;
				for (j=1 ; j<=n ; j++)
				{
					dp[0][j]=0;	
				}
				for (i=1 ; i<=n ; i++)
				{
					pp=p2[i];
					pp2=1-pp;
					dp[i][0]=dp[i-1][0]*pp2;
					for (j=1 ; j<i ; j++)
					{
						dp[i][j]=dp[i-1][j]*pp2+dp[i-1][j-1]*pp;
					}
					dp[i][i]=dp[i-1][i-1]*pp;
				}
				tempans=dp[k][k/2];
				
				ans=max(ans,tempans);
			}
		}
		printf("Case #%d: %f\n" ,ii ,ans);
	}
	
	return 0;
}
