#include <iostream>
#include <vector>
#include <iomanip>

#define eps 0.000001

using namespace std;

int t, n;
double v, x;
double r[100], c[100];
vector<int> u, d;
double utmp, dtmp, urt,drt, exrt;

int main() {
	cin >> t;
	cout << setprecision(15);
	for (int k=1;k<=t;k++) {
		cout << "Case #" << k << ": ";
		cin >> n >> v >> x;
		exrt = 0;
		u.clear();
		d.clear();
		for (int i=0;i<n;i++) {
			cin >> r[i] >> c[i];
			if (c[i] - x > eps) u.push_back(i);
			else if (x - c[i] > eps) d.push_back(i);
			else exrt += r[i];
		}

		if (!(exrt || (u.size() && d.size()))) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		if (!(u.size() && d.size())) {
			cout << v/exrt << "\n";
			continue;
		}
		urt = 0;
		utmp = 0;
		drt = 0;
		dtmp = 0;

		for (unsigned int i=0;i<u.size();i++) {
			utmp += c[u[i]]*r[u[i]];
			urt += r[u[i]];
		}
		for (unsigned int i=0;i<d.size();i++) {
			dtmp += c[d[i]]*r[d[i]];
			drt += r[d[i]];
		}
		utmp /= urt;
		dtmp /= drt;

		if (urt *(utmp-x) > drt*(x-dtmp)) {
			exrt += drt + (drt*(x-dtmp)/(utmp-x));
		} else {
			exrt += urt + (urt*(utmp-x)/(x-dtmp));
		}
		cout << v/exrt << "\n";
	}
}
