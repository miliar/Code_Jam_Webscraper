#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t, i, ans, c;
	bool ch;
	string s;

	freopen( "B-large.in", "r", stdin );
	freopen( "output1.txt", "w", stdout );

	scanf("%d", &t);

	int j = 0;
	while (j < t) {
        j++;
		cin>>s;
		s += '+';
		i = 0;
		ans = 0;

		while (i < s.length()) {
			c = 0;

			//cout<<s[i]<<endl;

			while (s[i] != '+') {
				c++;
				i++;
			}

			if (c > 0) ans++;
			if (s[i] == '+') {
				i++;
				break;
			}
		}

		//cout<<c<<endl;

		while (i < s.length()) {
			c = 0;

			while (s[i] != '+') {
				c++;
				i++;
			}

			if (c > 0) ans += 2;
			if (s[i] == '+') i++;
		}

		cout<<"Case #"<<j<<": "<<ans<<endl;
	}

	return 0;
}
