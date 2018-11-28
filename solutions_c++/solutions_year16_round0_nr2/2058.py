#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
using namespace std;

const int N = 200;

int n;

string s;

int ans;
int nowtd, tdnum;
int f[N], g[N];

void init_fg()
{
	int i, j;

	memset(f, 0, sizeof(f));
	memset(g, 0, sizeof(g));

	f[1] = 1;
	g[1] = 0;
	for (i = 2; i < N; i++)
		if (i & 1)
		{
			f[i] = 1 + g[i - 1];
			g[i] = min(1 + f[i - 1], g[i - 1]);
		}
		else
		{
			f[i] = min(1 + g[i - 1], f[i - 1]);
			g[i] = 1 + f[i - 1];
		}
}

void ri()
{
	cin >> s;
	while (s.find("++") != string::npos) s.replace(s.find("++"), 2, "+");
	while (s.find("--") != string::npos) s.replace(s.find("--"), 2, "-");
}

int solve()
{
	if (s[0] == '-') return f[s.size()]; else return g[s.size()];
}

void print()
{
	cout << "Case #" << nowtd << ": " << ans << endl;
}

int main()
{
	init_fg();
	cin >> tdnum;
	for (nowtd = 1; nowtd <= tdnum; nowtd++)
	{
		ri();
		ans = solve();
		print();
	}
	return 0;
}
