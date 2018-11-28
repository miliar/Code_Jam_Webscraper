#include<cstdio>
using namespace std;
int ans,n,stat;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t,lt;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		lt=0;
		stat=0;
		for(ans=1;ans<=200;ans++)
		{
			lt=n*ans;
			do
			{
				int temp=lt%10;
				stat=(stat)|(1<<temp);
				lt/=10;
			}while(lt);
			if(stat==1023||n==0)
				break;
		}
		if(n==0||stat==201)
			printf("Case #%d: INSOMNIA\n",i);
		else 
			printf("Case #%d: %d\n",i,ans*n);
	}
	return 0;
}
