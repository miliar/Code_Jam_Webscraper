#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void work()
{
	long double C, F, X;
	cin >> C >> F >> X;
	long double s = 0, d = 2, ans = 1e9;
	for (int i = 1; i <= 100001; ++i) {
		if (s + X / d < ans)
			ans = s + X / d;
		s += C / d;
		d += F;
	}
	cout << ans;
}

int main()
{		
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);

	cout << fixed;
	cout.precision(10);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}
