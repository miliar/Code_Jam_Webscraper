#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef pair<int, int> pii;
typedef long long int64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<int,pii> piii;

#define y1 dsjfksdj_fks
#define y2 alksaad_sa

int n, k;
string s;
int nt;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    
	int tn = 0;
	cin >> nt;
	for (;nt--;)
	{
		++tn;
		cin >> s >> k;
		int res = 0;
		n = static_cast<int>(s.length());
		for (int i = 0; i + k - 1 < n; ++i)
		{
			if (s[i] == '-')
			{
				++res;
				for (int j = i; j < i + k; ++j)
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		for (int i = 0; i < n; ++i)
			if (s[i] == '-')
				res = -1;
		cout << "Case #" << tn << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
    
    return 0;
}