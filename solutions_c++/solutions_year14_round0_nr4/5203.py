/* in the name of ALLAH, most gracious, most merciful */
using namespace std;

#include <cstdio>
#include <algorithm>
#include <set>

int n;
multiset <int> naomi, ken;

int cherry (bool flag = false) {
	auto a = naomi;
	auto b = ken;

	if (flag) swap (a, b);

	int ret = n;
	auto ai = a.begin ();
	auto bi = b.begin ();
	while (true) {
		if (a.empty () || b.empty ())
			break;
		if (*ai < *bi) {
			--ret;
			a.erase (ai);
			ai = a.begin ();
		}
		b.erase (bi);
		bi = b.begin ();
	}
	if (flag) ret = n - ret;
	return ret;
}

int main () {
#ifdef Local
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#endif

	int t;
	scanf ("%d", &t);
	
	for (int x = 1; x <= t; ++x) {
		scanf ("%d", &n);
		naomi.clear (); ken.clear ();

		for (int i = 0; i < 2 * n; ++i) {
			int u, v; scanf ("%d.%d", &v, &u);
			if (i < n) naomi.insert (u);
			else ken.insert (u); 
		}

		int y = cherry (true);
		int z = cherry ();
		printf ("Case #%d: %d %d\n", x, y, z);
	}

	return 0;
}

