#include <iostream>
#include <vector>
using namespace std;

int main() {
	int cs;
	cin >> cs;
	for (int cc = 1; cc <= cs; cc++) {
		int n;
		cin >> n;
		vector<int> d(n);
		int mx = 0;
		for (int i = 0; i < n; i++) {
			cin >> d[i];
			if (d[i] > mx)
				mx = d[i];
		}
		int rec = 999999999;
		for (int t = mx; t >= 1; t--) {
			int count = 0;
			vector<int> e(n);
			for (int i = 0; i < n; i++)
				e[i] = d[i];
			for (int i = 0; i < n; i++)
				while (e[i] > t) {
					e[i] -= t;
					count++;
				}
			if (count + t < rec)
				rec = count + t;
		}
		cout << "Case #" << cc << ": " << rec << "\n";
	}
}
