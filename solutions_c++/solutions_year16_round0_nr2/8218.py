//g++ -std=c++0x your_file.cpp -o your_program
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<math.h>
#include<vector>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<set>
#define fname ""
#define mp make_pair
#define F first
#define pb push_back
#define S second
#define ub upper_bound
#define lb lower_bound
#define inf 2000000000
#define INF 2000000000000000000ll
using namespace std;

string s;

inline void solve()
{
	cin >> s;
	int ans = 0;
	for (int i = (int)s.length() - 1; i >= 0; i--)
	{
		if (s[i] == '-')
		{
			for (int j = i; j >= 0; j--)
			{
				if (s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
			ans++;
		}
	}
//	cout << s << " ";
	printf("%d", ans);
}

int main()
{
	freopen (fname"input.txt", "r", stdin);
	freopen (fname"output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		if (i > 1)
			puts("");
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
