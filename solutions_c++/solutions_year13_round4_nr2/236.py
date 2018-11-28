#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int ca;
long long two[55];
long long n, p, a, b, c, d;

int main()
{
	freopen("b.out","w",stdout);
	two[0] = 1; 
	for (int i = 1; i < 55; i++) two[i] = two[i - 1] + two[i - 1];
	cin >> ca;
	for (int t = 1; t <= ca; t++) {
		cin >> n >> p;
		if (p == two[n]) a = two[n] - 1; else {
			a = 0; c = two[n - 1]; d = n - 1;
			while (c < p) {
				a += two[n - d];
				c += two[d - 1]; --d;
			}
		}
		b = 0; c = 1; d = n - 1;
		while (c + c <= p) {
			b += two[d];
			c += c; --d;
		}
		printf("Case #%d: ", t);
		cout << a << ' ' << b << endl;
	}
	return 0;
}

