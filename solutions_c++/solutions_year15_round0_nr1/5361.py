#include <cstdio>


int main()
{
	int T,len;
	char s[10000];
	int  c[10000],sum[10000];
	FILE *out=fopen("11.txt","w"); 
	scanf("%d",&T);
	for (int ncase=1;ncase<=T;ncase++)
	{
		fprintf(out,"Case #%d: ",ncase);
		scanf("%d",&len);
		scanf("%s",s);
		if (len==0)
		{
			fprintf(out,"0\n");
			continue;
		}
		
		for (int i=0;i<=len;i++) c[i]=s[i]-'0';
		
		int ans=0;
		sum[0]=c[0];
		for (int i=1;i<=len;i++)
		{
			if (sum[i-1]<i) ans+=i-sum[i-1],sum[i-1]=i;
			sum[i]=sum[i-1]+c[i];
		}
		fprintf(out,"%d\n",ans);
	}
	fclose(out);
	return 0;
} 
