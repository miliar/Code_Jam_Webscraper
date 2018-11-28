#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

int t, N;
double no;
vector<int> n, k, n2, k2;
char c;

int main() {
	scanf("%d", &t);

	for (int cc = 1; cc <= t; cc++) {
		printf("Case #%d: ", cc);
		scanf("%d", &N);
		n.clear(), k.clear();
		for (int i = 0; i < N; i++) {
			cin >> no;
			n.push_back((int)(no * 100000));
		}
		for (int i = 0; i < N; i++) {
			cin >> no;
			k.push_back((int)(no * 100000));
		}
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());
		n2 = n;
		k2 = k;
		
		int w2 = 0;
		for (int i = N - 1; i >= 0; i--) {
			no = n2[i];
			n2.erase(n2.begin()+i);

			if (no > k2[k2.size() - 1]) {
				k2.erase(k2.begin());
				w2++;
			}
			else {
				int tt = -1;
				for (int j = k2.size() - 1; j >= 0; j--)
					if (k2[j] > no)
						tt = j;
					else
						break;
				k2.erase(k2.begin() + tt);
			}
		}

		int w1 = 0;
		swap(n, k);
		for (int i = N - 1; i >= 0; i--) {
			no = n[i];
			n.erase(n.begin()+i);

			if (no > k[k.size() - 1]) {
				// cout << no << ' ' << k[0] << ' ' << 1 << endl;
				k.erase(k.begin());
				w1++;
			}
			else {
				int tt = -1;
				for (int j = k.size() - 1; j >= 0; j--)
					if (k[j] > no)
						tt = j;
					else
						break;
				// cout << no << ' ' << k2[tt] << ' ' << 0 << endl;
				k.erase(k.begin() + tt);
			}
		}

		printf("%d %d\n", N - w1, w2);
	}

	return 0;
}