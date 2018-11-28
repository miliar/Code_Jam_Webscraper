#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>

using namespace std;

int
main()
{
    int T;

    cin >> T;

    for (int i = 1; i <= T; ++i) {
	double C, F, X;

	cin >> C >> F >> X;

	int n = lrint(ceil(X / C - 1 - 2 / F));

	if (n < 0)
	    n = 0;

	double ans = 0;

	for (int j = 0; j < n; ++j)
	    ans += C / (2 + F * j);

	ans += X / (2 + F * n);

	printf("Case #%d: %.7lf\n", i, ans);
    }

    return 0;
}
