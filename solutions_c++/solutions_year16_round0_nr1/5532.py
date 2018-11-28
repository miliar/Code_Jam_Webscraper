#include <bits/stdc++.h>
using namespace std;
//typedef long long long long;
int tc, tcNum = 1;
bool taken[10];
void Solver();
int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	Solver();

}
void Solver() {
	cin >> tc;
	while (tc--) {
		long long n, temp, final;
		cin >> n;
		memset(taken, 0, sizeof taken);
		int count = 0, i = 1;
		cout << "Case #" << tcNum++ << ": ";
		if (n == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		while (count < 10) {
			final = temp = n * i;
			while (temp > 0) {
				if (!taken[temp % 10])
					count++, taken[temp % 10] = 1;
				temp /= 10;
			}
			i++;
		}
		cout << final << endl;
	}
}
