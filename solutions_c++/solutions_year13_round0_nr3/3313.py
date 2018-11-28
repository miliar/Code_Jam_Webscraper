#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

bool isPanli(int n) {
	vector<int> v;
	while (n > 0) {
		v.push_back( n % 10 );
		n /= 10;
	}

    for (int i = 0, j=v.size()-1; i < j; i++, j--) {
		if (v[i] != v[j])
			return false;
	}

	return true;
}

int solve() {
	// input
	int a, b;
	cin >> a >> b;
	int end = floor(sqrt(b));
	int ct = 0;
	for (int n = ceil(sqrt(a)); n <= end;  n++) {
		if (isPanli(n) && isPanli(n*n)) {
			// cout << n << " " << n*n << endl;
			ct++;
		}
	}

	return ct;
}

int main()
{
	int caseNum;
	cin >> caseNum;

	for (int caseNo=1; caseNo <= caseNum; ++caseNo) {
		int res = solve();
		cout << "Case #" << caseNo << ": " << res << endl;
	}
	return 0;
}
