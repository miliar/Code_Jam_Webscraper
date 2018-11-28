#include <iostream>

using namespace std;

typedef long long LL;

void solve()
{
	int n;
	cin >> n;
	if (n == 0) {
		cout << "INSOMNIA\n";
		return;
	}
	bool d[10] = {false};
	int dcnt = 0;
	LL pm = 0;
	while (dcnt < 10) {
		pm += n;
		LL m = pm;
		while (m > 0) {
			if (!d[m % 10]) dcnt++;
			d[m % 10] = true;
			m /= 10;
		}
	}
	cout << pm << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
