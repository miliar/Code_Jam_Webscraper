//In The Name Of Allah
//Code By Mona Mehdizadeh

#include <bits/stdc++.h>

using namespace std;

int main()
{
	int tt;
	cin >> tt;
	for (int ii = 0; ii < tt; ii ++)
	{
		int n;
		cin >> n;
		string s;
		cin >> s;
		int ans = 0 , stand = 0;
		for (int i = 0; i <= n; i ++)
		{
			if (stand < i)
			{
				ans += (i-stand);
				stand = i;
			}
			stand += (s[i]-'0');
		}
		cout << "Case #" << (ii+1) << ": " << ans << endl;
	}
	return 0;
}
