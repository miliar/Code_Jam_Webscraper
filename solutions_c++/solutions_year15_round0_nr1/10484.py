#include<cstdio>
using namespace std;

int main()
{
	int t,k;
	char s[1001];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		int n,sum=0,a=0;
		scanf("%d",&n);
		scanf("%s",s);
		sum=s[0]-'0';
		for(int i=1;i<=n;i++)
		{
			if(sum<i)
			{
				a++;
				sum+=s[i]-'0'+1;
			}
			else 
				sum+=s[i]-'0';
		}
		printf("Case #%d: %d\n",k,a);
	}
	return 0;
}
	