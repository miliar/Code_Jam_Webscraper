#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
#include <queue>
#include <cmath>
using namespace std;

int T;
long long p, q;
const int l = 2048;
long long a[l], b[l];
char c;

int f(long long n) {
	for (long long i = 0, j = 1; i <= 40; i++, j *= 2) {
		if (j == n) {
			return (int)i;
		}
	}
	return -1;
}

int main() {
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		printf("Case #%d: ", cc);

		cin >> p >> c >> q;
		long long lim = (long long)(sqrt(p + 0.0) + 1);
		for (long long i = 2; i <= lim; i++)
			while (p % i == 0 && q % i == 0) {
				p /= i;
				q /= i;
			}

		if (p != 1 && q % p == 0) {
			q /= p;
			p /= p;
		}

		int tmp = -1;
		if ((tmp = f(q)) == -1) {
			printf("impossible\n");
		}
		else {
			bool tf = (p == 1);
			int counta = 0, countb = 0, countc = 0;
			while (1) {
				if (p == 1) {
					break;
				}

				/*if (p * 2 >= q) {
					p -= (q / 2);
					counta++;
				}
				else {
					p--;
					countb++;
				}*/
				p--;
				countb++;

				if (p != 0 && p % 2 == 0 && q % 2 == 0) {
					while (p != 0 && p % 2 == 0 && q % 2 == 0) {
						p /= 2;
						q /= 2;
					}
				}

				// cout << p << ' ' << q << endl;
			}

			countc = f(q);

			// cout << countc - counta << ' ' << counta << ' ' << countb << ' ' << countc << endl;
			// cout << "c: " << counta << ' ' << countb << ' ' << countc << endl;
			cout << countc - counta << endl;// << endl;
		}
	}

	return 0;
}