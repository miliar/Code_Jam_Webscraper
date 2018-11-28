#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;

int main(void)
{
	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
	string str;
	ll t,j,cnt,ans,x=1;
	char sign;
	cin >> t;
	while(x<=t)
	{
		cin >> str;
		sign=str[0];
		j=0;
		cnt=0;
		ans=0;
		while(j < str.size())
		{
			if(sign == '+')
			{
				while(str[j]==sign && ++j < str.size())
					cnt++;
				if(j != str.size())
					ans++;
				sign='-';
			}
			else
			{
				while(str[j]==sign && ++j < str.size())
					cnt++;
				ans++;
				sign='+';
			}
		}
		cout << "Case #" << x << ": " << ans << "\n";
		x++;
	}
	return 0;
}