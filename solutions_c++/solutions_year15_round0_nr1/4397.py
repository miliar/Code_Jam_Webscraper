#include<cstdio>
#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	int c=1;
	while(t--)
	{
		int s;
		char str[1001];
		long long a[1001] = {0};
		scanf("%d %s",&s,str);
		a[0] = str[0]-'0';
		long long cnt = 0;
		for(int i=1;i<=s;i++)
		{
			if(i>a[i-1])
			{
				cnt += i -a[i-1] ;
				a[i] = i+str[i]-'0';
			}
			else a[i] = a[i-1]+str[i]-'0';
		}
		printf("Case #%d: %lld\n",c++,cnt);
	}
	return 0;
}
