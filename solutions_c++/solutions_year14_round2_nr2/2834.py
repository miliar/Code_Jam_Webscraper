#include <iostream>
#include <cstdio>
#include <fstream>//input output
#include <algorithm>
#include <functional>
#include <bitset>//technique
#include <cmath>
#include <iomanip>//useful
#include <string>
#include <cstring>//string
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>//ADT
using namespace std;

#define INF 2147483647
#define LL long long
#define For(i, n) for(int i = 0; i < n; ++i)

int main()
{
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k)
	{
		int a, b, c;
		cin >> a >> b >> c;
		int ans = 0;
		for (int da = 0; da < a; ++da)
		{
			for (int db = 0; db < b; ++db)
			{
				int x = da & db;
				if (x < c) ans++;
			}
		}
		cout << "Case #" << k << ": ";
		cout << ans << endl;

	}
	return 0;
}