#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include <unordered_set>

// =================== SOME USEFULL DEFINES ======================================
#define fi first
#define se second
#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define sqr(x) ((x)*(x))
#define pow2(x) (1 << (x))
#define hmap unordered_map
#define hset unordered_set
#define ll long long
// ===============================================================================

using namespace std;

istream& ioIN(int argc, const char **argv);
ostream& ioOUT(int argc, const char **argv);

int main(int argc, const char **argv) {
	istream &in = ioIN(argc, argv);
	ostream &out = ioOUT(argc, argv);

	int T;

	in >> T; //in.ignore();

	for (int t = 1; t <= T; ++t) {
		int n, m;
		in >> n >> m;
		int a[100][100];
		int rowMax[100] = { };
		int colMax[100] = { };
		bool wrong[100][100];

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				in >> a[i][j];
				wrong[i][j] = false;
				if (a[i][j] > rowMax[i])
					rowMax[i] = a[i][j];
				if (a[i][j] > colMax[j])
					colMax[j] = a[i][j];
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] < rowMax[i])
					wrong[i][j] = true;
			}
		}

		bool ok = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if ((wrong[i][j]) && (a[i][j] < colMax[j])) {
					ok = false;
					break;
				}
			}
		}

		out << "Case #" << t << ": " << (ok ? "YES" : "NO") << endl;
	}

	return 0;
}

// ===============================================================================

istream& ioIN(int argc, const char **argv) {
	if (argc > 1)
		return *(new ifstream(argv[1]));
	return cin;
}

ostream& ioOUT(int argc, const char **argv) {
	if (argc > 2)
		return *(new ofstream(argv[2]));
	return cout;
}
