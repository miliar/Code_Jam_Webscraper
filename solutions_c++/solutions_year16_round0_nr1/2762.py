#include<bits/stdc++.h>
using namespace std;
const int MAX = 1000010;
int a[MAX];

vector<int> decompose(int x) {
	vector<int> s;
	while (x > 0) {
		s.push_back(x % 10);
		x /= 10;
	}
	return s;
}

int check(int x) {
	unordered_set<int> s;
	for (int i = 1; i <= 100; ++i) {
		for (int val : decompose(x * i)) {
			s.insert(val);
		}
		if (s.size() == 10) {
			return x * i;
		}
	}
	return -1;
}

int main() {
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	memset(a, -1, sizeof(a));
	for (int testcase = 1; testcase <= T; ++testcase) {
		int x;
		cin >> x;
		printf("Case #%d: ", testcase);
		if (x != 0) {
			cout << check(x) << endl;
		} else {
			cout << "INSOMNIA" << endl;
		}
	}
//	for (int i = 1; i <= MAX; ++i) {
//		if (check(i) == -1) {
//			cout << i << endl;
//		}
//	}
	return 0;
}
