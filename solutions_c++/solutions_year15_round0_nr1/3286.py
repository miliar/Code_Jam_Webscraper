#include<cstdio>
#include<cstring>
using namespace std;
int Testcase,n;
char s[1024];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&Testcase);
	for(int t=1;t<=Testcase;++t)
	{
		scanf("%d",&n);
		scanf("%s",s);
		int num=0,sum=0;
		for(int i=0;i<=n;i++)
		{
			if(sum<i)
			{
				num+=i-sum;
				sum+=i-sum;
			}
			sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",t,num);
	}
}