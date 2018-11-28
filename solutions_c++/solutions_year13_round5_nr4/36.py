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

double f[1 << 20];

void work()
{
	string s;
	cin >> s;
	int n = s.size(), m = 0;
	for (int i = 0; i < n; ++i) 
		m = m * 2 + (s[i] == 'X' ? 1 : 0);	
	memset(f, 0, sizeof(f));
	for (int i = (1 << n) - 2; i >= 0; --i) {		
		double s = 0;
		for (int j = 0; j < n; ++j) {
			int k = j, cost = n;
			while (i & (1 << k)) {
				--k;
				--cost;
				if (k < 0)
					k = n - 1;
			}
			s += cost + f[i + (1 << k)];
		}		
		f[i] = s / n;
	}
	cout << fixed;
	cout.precision(15);	
	cout << f[m];
}

int main()
{
    freopen("d1.in", "r", stdin);
    freopen("d1.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);
        work();
        printf("\n");
    }
    
    return 0;
}
