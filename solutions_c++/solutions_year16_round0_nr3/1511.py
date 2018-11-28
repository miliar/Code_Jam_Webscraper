#include <bits/stdc++.h>
typedef long long LL;
using namespace std;
#define ALL(x) (x.begin(), x.end())
#define rep(i,n) for(int i = 0;i < n;i ++)

const int inf = 1e9;
int answer[55][11];

LL calc(int base, int mask) {
	LL ret = 0;
	for(int i = 15; ~i; i --) {
		ret *= base;
		if (mask >> i & 1) {
			ret += 1;
		}
	}
	return ret;
}

void Print(LL x) {
	if (x) {
		Print(x >> 1);
	} else {
		return;
	}
	cout << (x & 1 ? 1: 0);
}

int main() {
//	freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int T, N, J;
	cin >> T;
	rep(cas, T) {
		cin >> N >> J;
		cout << "Case #" << cas + 1 << ":";
		int tot = 1 << 16;
		int sum = 0;
		for(int mask = 1 << 15; mask < tot; mask ++) {
			if (mask & 1) {
				bool isprime = false;
				vector<int> temp;
				for(int base = 2; base <= 10; base ++) {
					LL number = calc(base, mask);
					bool flag = false;
					for(LL x = 2; x * x <= number; x ++) {
						if (number % x == 0) {
							temp.push_back(x);
							flag = true;
							break;
						}
					}
					if (!flag) {
						isprime = true;
						break;
					}
				}
				if (!isprime) {
					rep(j, temp.size()) {
						answer[sum][j] = temp[j];
					}
					answer[sum][10] = mask;
					sum ++;
				}
			}
			if (sum == 50) {
				break;
			}
		}
		/*cout << endl;
		rep(i, 50) {
			Print(answer[i][10]);
			rep(j, 9) {
				cout << " " << answer[i][j];
			}
			cout << endl;
		}*/
		cout << endl;
		sum = 0;
		rep(i, 50) {
			rep(j, 50) {
				vector<LL> temp;
				bool ok = true;
				for(int base = 2; base <= 10; base ++) {
					LL number = calc(base, answer[i][10]);
					LL number2 = calc(base, answer[j][10]);
					LL g = __gcd(number, number2);

					if (g == 1) {
						ok = false;
						break;
					} else {
						temp.push_back(g);
					}
				}
				if (ok) {
					sum ++;
					Print(answer[i][10]);
					Print(answer[j][10]);
					rep(j, temp.size()) {
						cout << " " << temp[j];
					}
					cout << endl;
				}
				if (sum == 500)	return 0;
			}
		}
	}
	return 0;
}

