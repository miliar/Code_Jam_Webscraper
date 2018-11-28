#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;

char q[4] = {'1', 'i', 'j', 'k'};
int prod[4][4] = {{1, 2, 3, 4},
									{2, -1, 4, -3},
									{3, -4, -1, 2},
									{4, 3, -2, -1}};

int abs(int a) {
	return max(a, -a);
}

int Prod(int qa, int qb) {
	return (qa < 0 ? -1 : 1) * (qb < 0 ? -1 : 1) * prod[abs(qa) - 1][abs(qb) - 1];
}

int Inv(int qa) {
	if (abs(qa) == 1) return qa;
	return -qa;
}

int Q(char c) {
	if (c == '1') return 1;
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
}

int main() {
	int t;
	cin >> t;
	for (int z = 1; z <= t; ++z) {
		VI sum(1, 1);
		int l, x;
		cin >> l >> x;
		string s; cin >> s;
		for (int i = 0; i < x; ++i) {
			for (int j = 0; j < l; ++j) {
				sum.push_back(Prod(sum.back(), Q(s[j])));
			}
		}
		
		bool ok = false;
		for (int i = 1; i < x * l; ++i) {
			for (int j = 1; i + j < x * l; ++j) {
				int q1 = sum[i];
				int q2 = Prod(Inv(sum[i]), sum[i + j]);
				int q3 = Prod(Inv(sum[i + j]), sum[x * l]);
				if (q1 == 2 and q2 == 3 and q3 == 4) {
					ok = true;
					break;
				}
			}
			if (ok) break;
		}
		cout << "Case #" << z << ": " << (ok ? "YES" : "NO") << endl;
	}
}