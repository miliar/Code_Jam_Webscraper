#include <iostream>
#include <set>
#include <fstream>
#include <vector>

using namespace std;

set<int> digits;
void parseNumber(long long x) {
	while (x > 0) {
		digits.insert(x % 10);
		x /= 10;
	}
}
long long  solve(long long n) {
	if (n == 0) return -1;
	digits.clear();
	int i = 1;
	long long m = n;
	while (digits.size() < 10)  {

		m = i * n;
		i++;
		parseNumber(m);

	}
	return m;
}

void output(int caseNum, long long res) {

	if (res == -1) {
		cout << "Case " << "#" << caseNum << ": " << "INSOMNIA" << endl;
	} else
	cout << "Case " << "#" << caseNum << ": " << res << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {

		long long n;
		cin >> n;

		output(t, solve(n));
	}

}
