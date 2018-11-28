#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair < double, int > pid;

vector < pid > v;

int n;
int t;

const int N = 1000;

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++) {
		printf("Case #%d: ", tt + 1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			double q;
			scanf("%lf", &q);
			v.pb(mp(q, 0));
		}
		for (int i = 0; i < n; i++) {
			double q;
			scanf("%lf", &q);
			v.pb(mp(q, 1));
		}
		sort(v.begin(), v.end());

		int indnaomi = 0;
		int indken = 0;

		int naomi = 0;
		vector < bool > used (N * 2, false);

		while (indnaomi < n * 2 && indken < n * 2) {
			while (indken < n * 2 && (v[indken].ss == 0 || used[indken]))
				indken++;
			while (indnaomi < n * 2 && (v[indnaomi].ss == 1 || used[indnaomi] || indnaomi < indken))
				indnaomi++;
			if (indnaomi == n * 2)	
				break;
			used[indnaomi] = true;
			used[indken] = true;

			naomi++;
			
		}


		printf("%d ", naomi);

		naomi = 0;

		indnaomi = 0;
		indken = 0;
		for (int i = 0; i < 2 * n; i++)
			used[i] = false;
		while (indnaomi < n * 2 && indken < n * 2) {
			while (indnaomi < n * 2 && (v[indnaomi].ss == 1 || used[indnaomi]))
				indnaomi++;
			while (indken < n * 2 && (v[indken].ss == 0 || used[indken] || indken < indnaomi))
				indken++;

			if (indken == n * 2)
				break;

			used[indnaomi] = true;
			used[indken] = true;

			//indnaomi++; indken++;
		}
		for (int i = 0; i < n * 2; i++)
				if (!used[i])
					naomi++;

		printf("%d\n", naomi / 2);

		v.clear();
	}



	return 0;
}