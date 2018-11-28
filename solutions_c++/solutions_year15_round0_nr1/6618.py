#include <bits/stdc++.h>
using namespace std;
int main() 
{
	char a[1000005];
	int i,j,k,l,n,m,t,sum=0,cnt=0;
	scanf("%d",&t);
	for(int yu=1;yu<=t;yu++)
	{
		printf("Case #%d: ",yu);
		sum=0;
		cnt=0;
		scanf("%d",&l);
		scanf("%s",a);
		for(i=0;i<=l;i++)
		{
			if(a[i]=='0')
				continue;
			else
			{
				if(cnt>=i)
					cnt+=a[i]-'0';
				else
				{
					sum+=i-cnt;
					cnt=i+a[i]-'0';
				}
			}
		}
		printf("%d\n",sum);
	}
	return 0;
}
