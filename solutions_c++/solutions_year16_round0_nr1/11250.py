#include "stdafx.h"
#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

void getNumber(int n, std::set<int>& s) {
	int k;
	while (n > 0) {
		k = n % 10;
		s.insert(k);
		n = n / 10;
	}
}

int work(int n) {
	set <int> s;
	int sum = 0;
	while (s.size() < 10) {
		sum += n;
		getNumber(sum, s);

	}
	return sum;

}

int main() {
	freopen("d://codejam//A-small-attempt0.in", "r", stdin);
	freopen("d://codejam//out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i += 1) {
		int x;
		scanf("%d", &x);
		cout << "Case #" << i + 1 << ": ";
		if (x == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int res = work(x);
		cout << res << endl;
	}
	return 0;
}
