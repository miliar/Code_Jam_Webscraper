#include <fstream>
#include <iomanip>

using namespace std;

double t[50001];

int main() {
	ifstream in("B-small-attempt0.in");
	ofstream out("B-small.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		double C, F, X; in >> C >> F >> X;
		t[0] = C / 2.0;
		double res = X / 2.0;
		for (double i = 1; i < 50001; i++) {
			int in = (int)i;
			t[in] = t[in - 1] + C / (2 + i * F);
		}

		for (double i = 1; i < 50001; i++) {
			int in = (int)i;
			double tmp = X / (2 + i * F);
			res = min(res, tmp + t[in - 1]);
		}
		out << "Case #" << x << ": " << fixed << setprecision(7) << res << endl;
	}

	return 0;
}
