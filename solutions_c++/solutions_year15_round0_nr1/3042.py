#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN=1010;
char str[MAXN];
int main()
{
	int t,n,i,flag=1;
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%s",&n,str);
		int sum=str[0]-'0';
		int ans=0;
		for(i=1;i<=n;i++)
		{
			if(sum>=i)
				sum+=str[i]-'0';
			else
			{
				ans+=i-sum;
				//printf("i=%d sum=%d\n",i,sum);
				sum=i+str[i]-'0';
			}
		}
		printf("Case #%d: %d\n",flag++,ans);
	}
	return 0;
}
