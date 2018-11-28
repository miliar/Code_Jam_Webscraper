#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <istream>
#include <map>
#include <numeric>
#include <ostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>


using namespace std;


// Powered by caide (code generator, tester, and library code inliner)

// variable definition here

int n, s;
int x[1024], y[1024], z[1024];
int vx[1024], vy[1024], vz[1024];

void initialize(std::istream &in) {
	// initialize variables here
	in >> n >> s;
	for (int i = 0; i < n; i++) {
		in >> x[i] >> y[i] >> z[i];
		in >> vx[i] >> vy[i] >> vz[i];
	}
}

double d[1024][1024];
double pi[1024];
bool chk[1024];
void solve_case(std::ostream &out) {
	// solve the case here
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++) {
			double dx = x[i] - x[j];
			double dy = y[i] - y[j];
			double dz = z[i] - z[j];
			d[i][j] = sqrt(dx * dx + dy * dy + dz * dz);
		}

	for (int i = 0; i < n; i++)
		pi[i] = 1e18;
	pi[0] = 0;
	memset(chk, 0, sizeof(chk));
	for (int i = 0; i < n; i++) {
		int v = -1; double min_pi = 1e20;
		for (int u = 0; u < n; u++) if (!chk[u]) {
			if (pi[u] < min_pi) {
				v = u;
				min_pi = pi[u];
			}
		}
		assert(v != -1);

		chk[v] = true;
		for (int u = 0; u < n; u++)
			pi[u] = min(pi[u], max(pi[v], d[u][v]));
	}
	out << pi[1] << endl;
}

void solve(std::istream& in, std::ostream& out) {
    out << std::setprecision(12);

	int T;
	in >> T;
	for (int t = 1; t <= T; t++) {
		cerr << "Case #" << t << " running" << endl;

		initialize(in);
		out << "Case #" << t << ": ";
		solve_case(out);

		cerr << "Case #" << t << " done" << endl;
	}
}


#include <fstream>


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);


    istream& in = cin;


    ostream& out = cout;

    solve(in, out);
    return 0;
}


