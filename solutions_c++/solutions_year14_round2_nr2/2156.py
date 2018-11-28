#include <fstream>

using namespace std;

int main() {
	ifstream fin("b.in");
	ofstream fout("b.out");
	int t, a, b, k, x, y, i, j;
	fin >> t;
	for(x = 1; x <= t; x++) {
		fin >> a >> b >> k;
		y = 0;
		for(i = 0; i < a; i++) for(j = 0; j < b; j++) if((i & j) < k) y++;
		fout << "Case #" << x << ": " << y << "\n";
	}
	return 0;
} 
