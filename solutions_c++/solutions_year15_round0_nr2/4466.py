#include <stdio.h>
#define inf 99999999

int f[1001][1001];


int main()
{
	int T,n;
	int c[1234];
	FILE *out=fopen("12.txt","w"); 
	scanf("%d",&T);
	for (int ncase=1;ncase<=T;ncase++)
	{
		fprintf(out,"Case #%d: ",ncase);
		int max=0;
		scanf("%d",&n);
	    for (int j=0;j<=1000;j++) f[0][j]=0;
	    for (int i=1;i<=1000;i++)
	      for (int j=1;j<=1000;j++) f[i][j]=inf;
	    
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&c[i]);
			int j=i-1;
	          for (int k=1;k<=1000;k++)
	          {
	          	 int t=c[i]/k-1;
	          	 if (c[i]%k!=0) t++;
	          	 if (f[j][k]+t<f[i][k]) f[i][k]=f[j][k]+t;
	          }
		}
		
		int ans=inf;
		for (int i=1;i<=1000;i++) 
		 if (ans>f[n][i]+i) ans=f[n][i]+i;
		 
		fprintf(out,"%d\n",ans);
		//printf("%d\n",ans);
	} 
	fclose(out);
	return 0;
} 



