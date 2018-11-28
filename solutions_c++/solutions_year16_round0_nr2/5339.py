#include <bits/stdc++.h>

#define ll long long
#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef pair < ll , ll > pie;

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	string s;
	cin >> T;
	for(int k = 1; k <= T; k++)
	{
		cin >> s;
		int res = 0,pri = 0, sec = 0, seen = 0;
		while(seen < s.size() && s[seen] == '-')
		{
			pri = 1;
			seen ++;
		}
		while(seen < s.size() && s[seen] == '+')
		{
			seen ++;
		}
		while(seen < s.size())
		{
			if(s[seen] == '-')
			{
				sec ++;
				while(seen < s.size() && s[seen] == '-')
					seen ++;
			}
			while(seen < s.size() && s[seen] == '+')
				seen ++;
		}
		res = pri + 2 * sec;
		cout << "Case #" << k << ": " << res << endl;
	}
	return 0;
}