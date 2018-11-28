#include <iostream>
#include <vector>
using namespace std;

long long getNumber(long long n) {
	vector<bool> seen(10, false);
	int nseen = 0;
	long long mul = 1;
	while (nseen < 10) {
		int t = n*mul;
		while (t > 0) {
			int num = t%10;
			if (!seen[num]) seen[num] = true, nseen++;
			t /= 10;
		}
		if (nseen == 10) return n*mul;
		mul++;
	}
	return n;
}

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		long long n;
		cin >> n;
		cout << "Case #" << cas << ": ";
		if (n == 0) cout << "INSOMNIA" << endl;
		else cout << getNumber(n) << endl;
	}
}
