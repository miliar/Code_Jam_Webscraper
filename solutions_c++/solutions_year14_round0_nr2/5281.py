#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

typedef long double lf;

void solve()
{
	lf curt = 0, curans = 1e100, cost, prof, x;
	cin >> cost >> prof >> x;
	for (int i = 0; i <= 300000; ++i)
	{
		curans = min(curans, curt + x / (prof * i + 2));
		curt += cost / (prof * i + 2);
	}
	cout << curans << endl;
}

int main() 
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout.precision(7);
	cout << fixed;
	int t;
    cin >> t;
    for (int i = 0; i < t; ++i) 
		cout << "Case #" << i + 1 << ": ", solve();
    return 0;
}

