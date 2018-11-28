#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,n;
	string s;
	freopen("a3.in","r",stdin);
	cin>>t;
	for (int j = 1; j <= t; ++j) {
		cin>>n;
		cin>>s;
		int ans = 0, coun = 0;
		for (int i = 0; i <= n; ++i) {
			int c = s[i] - '0';
			coun += c;

			if (coun <= i) {
				coun++;
				ans++;

			}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}