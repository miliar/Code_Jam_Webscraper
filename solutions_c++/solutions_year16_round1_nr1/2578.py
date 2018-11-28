#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:134217728")
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
#include <ctime>

typedef long long ll;

#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))
#define ZERO(x) memset((x), 0, sizeof(x))

using namespace std;

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int te;
	cin >> te;
	for (int w = 0; w < te; w++)
	{
		string s;
		cin >> s;
		string curs = string() + s[0];
		for (int i = 1; i < s.size(); i++)
		{
			if (s[i] + curs > curs + s[i])
				curs = s[i] + curs;
			else
				curs = curs + s[i];
		}
		printf("Case #%d: %s\n", w + 1, curs.c_str());
	}

	return 0;
}