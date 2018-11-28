#include <iostream>
#include <set>
#include <cstdio>
using namespace std;

void PrintAnswer(long long n) {
	if (n == 0) {
		cout <<"INSOMNIA";
		return;
	}
	set<int> numbers;
	long long mul = 1;
	while (numbers.size() != 10) {
		long long nn = n * mul;
		while (nn) {
			numbers.insert(nn % 10);
			nn /=10;
		}
		mul++;
	}
	cout << n * (mul - 1);
}
int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int t;
	long long n;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cin >> n;
		cout << "Case #" << tt <<": ";
		PrintAnswer(n);
		cout << endl;
	}
	return 0;
}
