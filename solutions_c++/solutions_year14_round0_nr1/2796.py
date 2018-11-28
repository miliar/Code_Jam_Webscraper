#include<bits/stdc++.h>
using namespace std;

#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))

const int OO = (int) 2e9;
const double EPS = 1e-9;

int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int t, ans;
	cin >> t;
	int g[4][4];
	for (int tt = 1; tt <= t; tt++) {
		vector<int> f(17, 0);
		for (int q = 0; q < 2; q++) {
			cin >> ans;
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++)
					cin >> g[i][j];

			for (int j = 0; j < 4; j++)
				f[g[ans - 1][j]]++;
		}

		vector<int> x;
		for (int i = 0; i <= 16; i++)
			if (f[i] == 2)
				x.push_back(i);

		printf("Case #%d: ", tt);
		if (SZ(x) == 1)
			cout << x[0] << endl;
		else if (SZ(x) > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
