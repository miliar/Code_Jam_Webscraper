#include <iostream>
using namespace std;

void cas() {
	int n; cin >> n;
	int m[1010];
	for (int i = 0; i < n; ++i) cin >> m[i];
	int y = 0, z = 0;
	for (int i = 1; i < n; ++i)
		if (m[i] < m[i-1]) y += m[i-1] - m[i];
	int rate = 0;
	for (int i = 1; i < n; ++i)
		if (m[i-1] - m[i] > rate) rate = m[i-1] - m[i];
	for (int i = 0; i < n-1; ++i) z += min(m[i], rate);
	cout << y << ' ' << z << endl;
}

int main() {
	int t; cin >> t;
	int i = 1;
	while (t--) {
		cout << "Case #" << i++ << ": ";
		cas();
	}
}
