#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include <vector>

#define mp make_pair
#define pb push_back
#define f first
#define s second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int N = (int)(1e5) + 7;
const int mod = (int)(1e9) + 7;
const ld eps = 1e-15;

string s[4];

bool prov1()
{
	for (int i = 0; i < 4; ++i)
	    for (int j = 0; j < 4; ++j)
	        if (s[i][j] == '.')
	            return 0;
	return 1;
}

bool prov(char x)
{
	for (int i = 0; i < 4; ++i)
	{
		bool f = 0, f1 = 0;
		for (int j = 0; j < 4; ++j)
		{
		    if (s[i][j] != x && s[i][j] != 'T')
				f = 1;
			if (s[j][i] != x && s[j][i] != 'T')
				f1 = 1;
		}
		if (!f || !f1)
		    return 1;
	}
	bool f = 0, f1 = 0;
	for (int i = 0; i < 4; ++i)
	{
		if (s[i][i] != x && s[i][i] != 'T')
			f = 1;
		if (s[i][3 - i] != x && s[i][3 - i] != 'T')
			f1 = 1;
	}
	if (!f || !f1)
	    return 1;
	return 0;
}

int main()
{
	int n;
	cin >> n;
	for (int qq = 0; qq < n; ++qq)
	{
		cout << "Case #" << qq + 1 << ": ";
		for (int i = 0; i < 4; ++i)
		    cin >> s[i];
		if (prov('X'))
		{
			cout << "X won\n";
			continue;
		}
		if (prov('O'))
		{
			cout << "O won\n";
			continue;
		}
		if (prov1())
		{
			cout << "Draw\n";
			continue;
		}
		cout << "Game has not completed\n";
	}
    return 0;
}
