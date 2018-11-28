#include<stdio.h>
double D[21][1048576];
double p;
char a[30];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,TC,T=0,k,t,S,tt;
	for(i=1;i<=20;i++)
	{
		p=1.0/i;
		for(j=1;j<(1<<i);j++)
		{
			for(k=0;k<i;k++)
			{
				if((1<<k)&j)break;
			}
			t=k,tt=k+i;
			for(k=i-1;k>=0;k--){
				if((1<<k)&j)t=tt=k;
				D[i][j]+=p*(D[i][j-(1<<t)]+i-tt+k);
			}
		}
	}
	scanf("%d",&TC);
	while(TC--){
		printf("Case #%d: ",++T);
		scanf("%s",a);
		S=0;
		for(i=0;a[i];i++){
			if(a[i]=='.')S+=1<<i;
		}
		printf("%.10lf\n",D[i][S]);
	}
}