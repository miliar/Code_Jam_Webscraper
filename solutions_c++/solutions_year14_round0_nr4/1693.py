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

const int maxn = 1000 + 5;

int n;
double a[maxn], b[maxn];

int calc(double *a, double *b)
{
	int k = n;
	for (int i = n; i >= 1; --i)
		if (b[k] >= a[i]) 			
			--k;
	return k;
}

void work()
{
	cin >> n;
	for (int i = 1; i <= n; ++i)
		cin >> a[i];
	for (int i = 1; i <= n; ++i)
		cin >> b[i];
	sort(a + 1, a + n + 1);
	sort(b + 1, b + n + 1);
	cout << n - calc(b, a) << " " << calc(a, b);
}

int main()
{
    freopen("d2.in", "r", stdin);
    freopen("d2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}

