#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <utility>
#include <ctime>
#include <string>
#include <sstream>
#include <queue>
#include <cstring>
#include <functional>

using namespace std;
typedef long long ll;
typedef long double ld;
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int te;
	cin >> te;
	for (int q = 0; q < te; q++)
	{
		int n, l;
		cin >> n >> l;
		set<string> G;
		for (int i = 0; i < n; i++)
		{
			string s;
			cin >> s;
			G.insert(s);
		}
		string B;
		cin >> B;

		printf("Case #%d: ", q + 1);

		if (G.count(B))
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << 0;
			for (int i = 0; i < l - 1; i++) cout << "?";
			cout << ' ';
			for (int i = 0; i < l / 2 + 1; i++)
			{
				cout << 1 << 0;
			}
			cout << "?";
			for (int i = 0; i < l / 2 + 1; i++)
			{
				cout << 1 << 0;
			}
		}
		cout << endl;

	}

	return 0;
}