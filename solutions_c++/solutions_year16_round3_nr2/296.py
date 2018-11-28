#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;

bool found;
char f[100][100];


void solve() {
	int b;
	long long m;
	cin >> b >> m;
	
	static int test_id;
	++test_id;

	found = (1LL << (b - 2)) >= m;
	memset(f, 0, sizeof f);
	for (int i = 1; i < b; ++i) {
		for (int j = 0; j < b; ++j)
			f[i][j] = '0';
		for (int j = i + 1; j < b; ++j)
			f[i][j] = '1';
	}
	if (m) {
		--m;
		f[0][b-1] = '1';
	} else {
		f[0][b-1] = '0';
	}
	for (int i = b - 2; i > 0; --i) if (m & (1LL << (b - 2 - i))) {
		f[0][i] = '1';
	} else {
		f[0][i] = '0';
	}
	f[0][0] = '0';
	
//	cout << b << ' ' << m + 1 << endl;
	cout << "Case #" << test_id << ": ";
	
	if (found) {
		cout << "POSSIBLE" << endl;
		for (int i = 0; i < b; ++i)
			cout << f[i] << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}

int main() {
	int t;
	cin >> t;
	while (t -->0) solve();
	return 0;
}