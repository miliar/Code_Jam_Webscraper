#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;

bool v[10];

long long int get_a(long long int n) {
	memset(v, 0, 10);
	int cnt = 1, k;
	long long int z = n, g;
	while (cnt < 11) {
		//ans++;
		g = z;
		while (g != 0) {
			k = g % 10;
			if (!v[k]) {
				cnt++;
				v[k] = true;
			}
			g /= 10;
		}
		z += n;
	}
	return z-n;
}

int main()
{
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		long long int n;
		cin >> n;
		cout << "Case #" << t << ": ";
		if (n > 0) {
			cout << get_a(n);
		}
		else {
			cout << "INSOMNIA";
		}

		cout << endl;
	}
	//system("pause");
	return 0;
}