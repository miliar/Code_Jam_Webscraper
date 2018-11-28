#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	ios::sync_with_stdio(false);

	int test_num;
	cin >> test_num;
	for (int itest = 0; itest < test_num; itest++) {
		int n;
		string s;
		cin >> n >> s;
//		cerr << n << s[0] << endl;
		int cur = s[0] - '0';
		int inv = 0;
		for (int i = 1; i <= n; i++) {
			int num = s[i] - '0';
			if (num == 0) continue;
			if (cur < i) {
				int dcur = i - cur;
				cur += dcur;
				inv += dcur;
			}
			cur += num;
		}
		cout << "Case #" << itest + 1 << ": " <<  inv << endl;
	}

	return 0;
}
