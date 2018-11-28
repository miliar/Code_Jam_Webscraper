/*
ID: alperca1
LANG: C++
TASK: dualpal
*/

#include <bits/stdc++.h>

#ifdef NOT_UVA
#include <Windows.h>
#endif

using namespace std;

typedef unsigned long long ull;
typedef pair<ull, int> ulli;
typedef pair<int, int> ii;

#define INF (1<<30)

double pi = 3.14;



int main(int argc, char **argv)
{
	//ios_base::sync_with_stdio(false);
#ifndef NOT_UVA
	//freopen("daireler.gir", "r", stdin);
	freopen("daireler.cik", "w", stdout);
#endif
	freopen("daireler.cik", "w", stdout);
	int t;
	cin >> t;
	int no = 1;
	while (t--)
	{
		string s;
		cin >> s;

		int count[500] = { 0 };
		int cc[15] = { 0 };

		for (int i = 0; i < s.length(); ++i)
		{
			++count[s[i]];
		}

		cc[0] = count['Z'];
		cc[4] = count['U'];
		cc[8] = count['G'];
		cc[5] = count['F'] - cc[4];

		cc[6] = count['X'];
		cc[3] = count['H'] - cc[8];
		cc[2] = count['W'];
		cc[1] = count['O'] - cc[4] - cc[2]-cc[0];
		cc[9] = count['I'] - cc[5] - cc[6] - cc[8];
		cc[7] = count['N'] - cc[1] - 2*cc[9];
		string res = "";
		for (int i = 0; i < 10; ++i)
		for (int j = 0; j < cc[i]; ++j)
		{
			res += ('0' + i);
		}

		cout << "Case #" << no++ << ": " << res << endl;
	}

	
#ifdef NOT_UVA
	//Sleep(-1);
#endif

	return 0;
}

