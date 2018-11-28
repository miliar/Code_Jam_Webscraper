#include <bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define pi 3.14159265
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define MEM(x, y) memset(x, y, sizeof(x))
using namespace std;

ll powten[15];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	powten[0] = 10;
	for (int i = 2; i <= 15; i++) {
		powten[i] = 10 * powten[i - 1];
	}

	ll tc, n, seen[10] = {0}, temp;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		cin >> n;
		cout << "Case #" << t << ": ";
 		if (n == 0) {
			cout << "INSOMNIA\n";
			continue;
		}
		MEM(seen, 0);
		for (int i = 0; i < 100; i++) {
			temp = n * i;
			int q = 0, x;
			while (temp != 0) {
				x = temp % 10;
				seen[x] = 1;
				temp = temp / 10;
			}
			x = 0;
			for (int p = 0; p < 10; p++) {
				if (seen[p] == 0) {
					x = 1;
					break;
				}
			}
			if (x == 0) {
				temp = n * i;
				break;
			}
		}
		cout << temp << endl; 
	}
	return 0;
}