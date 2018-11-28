#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <set>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)

typedef pair <int, int> PII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t;
	cin >> t;
	FOR(tt,t) {
		int r[2];
		vector<int> count(16);
		cin >> r[0];
		r[0]--;
		VVI a(4, VI(4));
		VVI b(4, VI(4));
		FOR(i,4) FOR(j,4) {
			cin >> a[i][j];
			a[i][j]--;
		}
		cin >> r[1];
		r[1]--;
		FOR(i,4) FOR(j,4) {
			cin >> b[i][j];
			b[i][j]--;
		}

		FOR(i,4) {
			count[a[r[0]][i]]++;
			count[b[r[1]][i]]++;
		}
		std::vector<int> x;
		FOR(i, 16) {
			if (count[i] == 2) {
				x.push_back(i + 1);
			}
		}

		cout << "Case #" << tt + 1 << ": ";
		if (x.size() == 1) {
			cout << x[0];
		}

		if (x.size() == 0) {
			cout << "Volunteer cheated!";
		}

		if (x.size() > 1) {
			cout << "Bad magician!";
		}



		cout << endl;
	}
    return 0;
}