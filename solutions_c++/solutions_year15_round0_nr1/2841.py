#include<cstdio>
#include<cstring>
using namespace std;
int n;
char a[1010];
int sum[1010];
void work(int lab)
{
	printf("Case #%d: ",lab);
	scanf("%d",&n);
	scanf("%s",a);
	memset(sum,0,sizeof(sum));
	for (int i=0;i<=n;i++)
	{
		sum[i]=a[i]-'0';
	}
	int ans=0;
	int tot=0;
	for (int i=0;i<=n;i++)
	{
		if (tot<i)
		{
			ans+=i-tot;
			tot=i+sum[i];
		}
		else tot+=sum[i];
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)work(i);
	return 0;
}
