#include <stdio.h>
#include <string.h>
using namespace std;
void zhuan(char a[],long long b[],long long len)
{
	int i;
	for(i=len-1;i>=0;i--)
	{
		b[i]=a[i]-'0';
	}
}
int main()
{
	freopen("F:\\TestFiles\\A-large.in","r",stdin);
	freopen("F:\\TestFiles\\A-large.out","w",stdout);
	char a[99999];
	long long b[99999];
	long long n,i,maxs,j;
	int t;
	while(scanf("%d",&t)!=EOF)
	{
		
		for(i=1;i<=t;i++)
		{
			long long count=0;
			long long ans=0;
			long long num=0;
		scanf("%lld",&maxs);
		getchar();
		gets(a);
		long long len=strlen(a);
		zhuan(a,b,len);
		for(j=0;j<len;j++)
		{
			num+=b[j];
			if(num<j+1)
			{
				ans+=j+1-num;
				count+=ans;
				num+=ans;
				ans=0;
			}
		}
		printf("Case #%lld: %lld\n",i,count);
	}
}
	return 0;
}
