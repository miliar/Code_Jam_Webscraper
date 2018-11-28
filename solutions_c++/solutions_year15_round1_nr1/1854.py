#include <fstream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large-1.out");

	int T;
	in >> T;

	for (int x = 1; x <= T; x++) {
		long long y = 0, z = 0;

		int N; in >> N; long long m[N]; for (int i = 0; i < N; i++) in >> m[i];

		long long mx = 0;
		for (int i = 0; i < N - 1; i++) if (m[i] > m[i + 1]) y += m[i] - m[i + 1], mx = max(mx, m[i] - m[i + 1]);

		for (int i = 0; i < N - 1; i++) {
			if (m[i] <= mx) z += m[i];
			else z += mx;
		}

		out << "Case #" << x << ": " << y <<  " " << z << endl;
	}

	return 0;
}
