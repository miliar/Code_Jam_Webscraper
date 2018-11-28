#include <fstream>
#include <algorithm>

using namespace std;

ifstream in("din.in");
ofstream out("dout.out");

const int N = 1001;

double a[N];
double b[N];
bool used[N];
int n;

bool find(double x, int mn) {
	for (int i = mn; i < n; ++i) {
		if (!used[i] && b[i] > x) {
			used[i] = true;
			return true;
		}
	}

	return false;
}

void solve(int test) {
	out << "Case #" << test << ": ";
	in >> n;
	for (int i = 0; i < n; ++i) {
		in >> a[i];
	}
	for (int i = 0; i < n; ++i) {
		in >> b[i];
	}

	sort(a, a+n);
	sort(b, b+n);

	int lpb = 0;
	int lpa = 0;
	int wins = 0;
	memset(used, 0, sizeof(used));

	while (lpa < n) {
		if (a[lpa] > b[lpb]) {
			++wins;
			++lpb;
		}
		++lpa;
	}

	out << wins << " ";

	wins = 0;
	lpb = 0;
	for (int i = n-1; i >= 0; --i)
		if (find(a[i], lpb) == false) {
			++wins;
			++lpb;
		}

	out << wins << "\n";
}

int main() {
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i) {
		solve(i);
	}

	return 0;
}
