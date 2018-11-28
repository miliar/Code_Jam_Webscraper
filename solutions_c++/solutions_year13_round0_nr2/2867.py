#include <fstream>

using namespace std;

ifstream in("in");
ofstream out("out");

const int N = 101;

int n, m;
int v[N][N];
int mx[N];
int my[N];

int main() {
	int t;
	in >> t;

	for (int cur = 1; cur <= t; ++cur) {
		in >> n >> m;
		int lim = (n>m ? n:m);
		for (int i = 0; i < lim; ++i)
			mx[i] = my[i] = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				in >> v[i][j];

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j) {
				if (v[i][j] > mx[i])
					mx[i] = v[i][j];
				if (v[i][j] > my[j])
					my[j] = v[i][j];
			}

		bool good = true;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (mx[i] > v[i][j] && my[j] > v[i][j])
					good = false;

		out << "Case #" << cur << ": ";
		if (good == true)
			out << "YES\n";
		else
			out << "NO\n";
	}

	return 0;
}
