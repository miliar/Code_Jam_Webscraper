#include <iostream>
using namespace std;

int main() {
	int cs;
	cin >> cs;
	for (int cc = 1; cc <= cs; cc++) {
		int x, r, c;
		cin >> x >> r >> c;
		bool rich = false;
		if ((r * c) % x != 0)
			rich = true;
		if (x > max(r, c))
			rich = true;
		if (min(r, c) * 2 <= x && min(r, c) > 1)
			rich = true;
		if (min(r, c) * 2 + 1 <= x)
			rich = true;
		if (x >= 7)
			rich = true;
		cout << "Case #" << cc << ": " << (rich ? "RICHARD" : "GABRIEL") << "\n";
	}
}
