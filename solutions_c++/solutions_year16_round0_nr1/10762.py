#include <bits/stdc++.h>

using namespace std;
int main(void)
{
	int t,c,i,flag,j;
	long long int n,num;
	string s;
	scanf("%d",&t);
	j=0;
	while(j++<t)
	{
		printf("Case #%d: ",j);
		flag=0;
		int count[10]={0};
		c=0;
		scanf("%lld",&n);
		if(n==0)
		{
				printf("INSOMNIA\n");
			continue;
		}
		num=n;
		while(1)
		{
			s=std::to_string(num);
			for(i=0;i<s.length();i++)
			{
				if(count[s[i]-48]==0)
				{
					count[s[i]-48]++;
					c++;
				}
				if(c==10)
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
				break;
			else
				num+=n;
	}
		printf("%lld\n",num);
	}
	return 0;
}
