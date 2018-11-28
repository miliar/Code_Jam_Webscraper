#include <fstream>
#include <cstdlib>

using namespace std;

ifstream in("lot.in");
ofstream out("lot.out");

const int N = 1005;
int c[N];

int main() {
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i) {
		int a, b, k;
		in >> a >> b >> k;

		memset(c, 0, sizeof(c));

		for (int l = 0; l < a; ++l)
			for (int j = 0; j < b; ++j)
				++c[l&j];

		int res = 0;
		for (int l = 0; l < k; ++l)
			res += c[l];

		out << "Case #" << i << ": " << res << "\n";
	}

	return 0;
}
