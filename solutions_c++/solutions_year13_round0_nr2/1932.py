#include <iostream>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vii;

int main() {
	int t, n, m, ai, aj;
	cin >> t;
	for (int cases = 1; cases <= t; ++cases) {
		cin >> n >> m;
		vii v(n, vi(m));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				cin >> v[i][j];

		bool pos = true;
		int i = 0;
		while (i < n and pos) {
			int j = 0;
			while (j < m and pos){
				bool posi = true;
				bool posj = true;
				for (int ai = 0; ai < n; ++ai){
					if (v[ai][j] > v[i][j])
						posi = false;
				}
				for (int aj = 0; aj < m; ++aj){
					if (v[i][aj] > v[i][j])
						posj = false;
				}

				pos = (posi or posj);
				++j;

			}
			++i;
		}

		if (pos) cout << "Case #" << cases << ": YES" << endl;
		else cout << "Case #" << cases << ": NO" << endl;
	} 
}