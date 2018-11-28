#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

long long ex[60];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	ex[0] = 1;
	for (int i = 1; i <= 50; i++) ex[i] = ex[i - 1] * 2;
	int T, TT = 0;
	cin >> T;
	while (T--) {
		long long n, p;
		cin >> n >> p;
		cout << "Case #" << ++TT << ": ";
		if (p != ex[n]) {
			long long k, i;
			for (i = p, k = n; i > 0; k--) i -= ex[k - 1];
			cout << ex[n - k] - 2 << " ";
			for (i = ex[n], k = n; i > p; k--) i -= ex[k - 1];
			cout << ex[n] - ex[n - k] << endl;
		}
		else cout << ex[n] - 1 << " " << ex[n] - 1 << endl;
	}
	return 0;
}
