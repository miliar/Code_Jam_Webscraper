#include <fstream>
#include <cstdlib>

using namespace std;

const int N = 17;
int v[N];
int a[N][N];

ifstream in("input.txt");
ofstream out("output.txt");

void readMatrix() {
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			in >> a[i][j];
}

void solve(int tc) {
	memset(v, 0, sizeof(v));
	int doIt = 2;

	while (doIt--) {
		int curRow;
		in >> curRow;
		--curRow;

		readMatrix();
		for (int i = 0; i < 4; ++i)
			++v[a[curRow][i]];
	}

	int ans;
	int no = 0;

	for (int i = 0; i < N; ++i) {
		if (v[i] == 2) {
			++no;
			ans = i;
		}
	}

	out << "Case #" << tc << ": ";

	if (no == 1)
		out << ans << "\n";
	else if (no > 1)
		out << "Bad magician!\n";
	else
		out << "Volunteer cheated!\n";
}

int main() {
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i) {
		solve(i);
	}

	return 0;
}

