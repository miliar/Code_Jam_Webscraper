#include<cstdio>
#define N 10
int test,n,j,flag[N],k,cnt,ii;
long long m,ans;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&test);
	while (test--)
	{
		scanf("%d",&n);
		ans=0;
		ii++;
		for (j=0;j<=9;j++)
		flag[j]=0;
		printf("Case #%d: ",ii);
		for (j=1;j<=100000;j++)
		{
			cnt=0;
			m=(long long)n*j;
			while (m)
			{
				flag[m%10]=1;
				m/=10;
			}
			for (k=0;k<=9;k++)
			cnt+=flag[k];
			if (cnt==10) 
			{
				ans=(long long)n*j;
				break;
			}
		}
		if (ans==0)
		printf("INSOMNIA\n");
		else
		printf("%I64d\n",ans); 
	}
}
