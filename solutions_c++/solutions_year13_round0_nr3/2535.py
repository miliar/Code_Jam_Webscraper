#include <iostream>
#include <sstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;
typedef long long LL;

int is_palindrome(LL i) {
	stringstream ss;
	ss << i;
	string s = ss.str();
	string t = s;
	reverse(t.begin(), t.end());
	if (s == t) return 1;
	else return 0;
}

int main() {
	vector<LL> vll;
	for (LL i = 1; i <= 4000000; i++) {
		if (is_palindrome(i) && is_palindrome(i*i)) {
			vll.push_back(i*i);
		}
	}

	int sz = vll.size();
	cout << "calculations is finised" << endl;

	int T; scanf("%d", &T);
	stringstream ss;
	for (int i = 0; i < T; i++) {
		ss << "Case #" << i+1 << ": ";

		long long A, B; scanf("%lld %lld", &A, &B);

		int cnt = 0;
		for (int j = 0; j < sz; j++) {
			if (A <= vll[j] && vll[j] <= B) cnt++;
		}

		ss << cnt << endl;
	}

	ofstream ofs("output.txt");
	cout << ss.str();
	ofs << ss.str();
	return 0;
}
