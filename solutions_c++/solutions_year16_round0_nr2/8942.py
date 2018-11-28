#include<bits/stdc++.h>
using namespace std;
int main()
{
	int tc,ans,cnt,l;
	string s;
	cin >> tc;
	for(int x=1;x<=tc;x++)
	{
		cin >> s;
		ans = 0;
		l=s.length();
		for(int i=l-1;i>=0;i--)
		{
			/*cnt=0;
			for(int j=0;j<l;j++)
			{
				if(s[j]=='+')
					cnt++;
			}
			if(cnt==l)
				break;*/
			if(s[i]=='-')
			{
				ans++;
				for(int j=0;j<=i;j++)
				{
					if(s[j]=='+')
						s[j]='-';
					else
						s[j]='+';
				}
			}

		}
		cout << "Case #" << x << ": " << ans << "\n";
	}
	return 0;
}
