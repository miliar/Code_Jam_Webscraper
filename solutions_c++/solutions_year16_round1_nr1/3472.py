#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("archivo.in","r",stdin);
	freopen("archivo.out","w",stdout);
	int t;
	cin >> t;
	for ( int tc = 1 ; tc <= t ; tc ++ )
	{
		string s;
		cin >> s;
		string ans = "";
		ans+=s[0];
		for ( int i = 1 ; i < s.size() ; i ++ )
		{
			if ( ans[0] <= s[i] )
				ans = s[i] + ans;
			else
				ans += s[i];
		}
		cout << "Case #"<<tc<<": "<<ans<<endl;
	}
}
