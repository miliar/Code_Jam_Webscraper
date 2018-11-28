#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		string s;
		cin >> s;
		int l = s.length();
		int inv = 0;
		int add = 0;
		if (s[l - 1] == '-')
			add = 1;

		for (int i = 0; i < l; i++)
		{
			if (s[i + 1] != s[i] && i + 1 < l)
			{
				inv++;
				//i++;

			}
		}

		cout << "Case #" << tt << ": " << (inv + add) << endl;
	}

	return 0;
}
