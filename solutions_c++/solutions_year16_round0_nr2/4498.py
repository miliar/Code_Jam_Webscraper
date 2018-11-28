#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("pan_large.out","w",stdout);
	char sign;
	string str;
	long long t,j=0,ans,cnt,k=0;
	scanf("%lld",&t);
	while(t--)
	{
		j=0;cnt=0;ans=0;
		cin>>str;
		if(str[0]=='-')
			sign='-';
		else
			sign='+';		
		while(j<str.length())
		{
			cnt=0;
			if(sign=='-')
			{
				cnt++;
				while(++j<str.length()&&str[j]==sign)
					cnt++;
				ans++;
				sign='+';
			}
			else
			{
				cnt++;
				while(++j<str.length()&&str[j]==sign)
					cnt++;
				if(j!=str.length())
					ans++;
				sign='-';
			}
		}
		printf("Case #%lld: %lld\n",++k,ans);
	}
	return 0;
}			
		
