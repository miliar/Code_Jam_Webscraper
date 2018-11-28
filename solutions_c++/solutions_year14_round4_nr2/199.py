#include <set>
#include <iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int main(void)
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ti++) {
		int n;
		cin >> n;
		vector<int> v(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}
		int ret = 1000000;
		for (int x = 0; x < (1<<n); x++) {
			int d = 0;
			for (int i = 0; i < n; i++) {
				int ai = (x&(1<<i)) != 0 ? 1 : 0; // 1 if down
				for (int j = i+1; j < n; j++) {
					int aj = (x&(1<<j)) != 0 ? 1 : 0;
					if (ai > aj) d++;
					else if (ai == aj) {
						if (ai == 0 && v[i] > v[j]) d++;
						else if (ai == 1 && v[i] < v[j]) d++;
					}
				}
			}
			if (d < ret) ret = d;
		}
		cout << "Case #" << ti << ": " << ret << endl << flush;
	}
	return 0;
}
