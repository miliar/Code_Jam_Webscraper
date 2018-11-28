#include <fstream> 

using namespace std;

int main() {
	int x, r, c;
	int t;
	fstream f; f.open("a.txt");
	fstream f2; f2.open("output.txt", ios::out);
	f >> t;
	int n = t;
	while (t--) {
		f >> x >> r >> c;
		bool gabrielWins = true;
		if (r*c % x != 0)						// We need to cover the area so the tiles should be a factor.
			gabrielWins = false;
		if (r*c == x && (x == 3 || x == 4))		// empirical
			gabrielWins = false;
		if (r*c == 8 && x == 4)					// exception/
			gabrielWins = false;
		f2 << "Case #" << n - t << ": ";
		(gabrielWins) ? f2 << "GABRIEL\n" : f2 << "RICHARD\n";
	}
	return 0;
}