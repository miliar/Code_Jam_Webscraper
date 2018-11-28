#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int bits(int k) {
	return 1 << k;
}

int setbit(int x, int k) {
	return x | bits(k);
}

int getDigitHash(int x) {
	int ret = 0;
	while (x) {
		ret = setbit(ret, x%10);
		x /= 10;
	}
	return ret;
}

int main() {
	ifstream in("A-large.in");
	cin.rdbuf(in.rdbuf());
	ofstream out("A-large.out");
	cout.rdbuf(out.rdbuf());
	// init table
	vector<int> table;
	table.push_back(-1);
	for (int i = 1; i <= 1e6; ++i) {
		int times = 0, hash = 0;
		do {
			hash |= getDigitHash(i * ++times);
		} while (hash != 1023 && times <= 75);
		if (times < 75) table.push_back(i * times);
		else table.push_back(-1);
	}
	// read
	int kase = 1, n, x, v;
	cin >> n;
	while (n--) {
		cin >> x;
		v = table[x];
		cout << "Case #" << kase++ << ": ";
		if (v != -1) cout << v << endl;
		else cout << "INSOMNIA" <<endl;
	}
}