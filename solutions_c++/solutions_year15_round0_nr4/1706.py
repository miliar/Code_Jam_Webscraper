#include <iostream>
#include <cstdint>

using namespace std;

bool assholeblock(uint64_t nom, uint64_t x, uint64_t y) {
	if ((x*y) % nom != 0)
		return true;
	switch (nom) {
	case 0:
		return false;
	case 1:
		return false;
	case 2:
		if (x < 2 && y < 2)
			return true;
		return false;
	case 3:
		if (x == 1 || y == 1 || (x < 3 && y < 3))
			return true;
		return false;
	case 4:
		if (x <= 2 || y <= 2 || (x < 4 && y < 4))
			return true;
		return false;
	case 5:
		if (x <= 3 || y <= 3 || (x < 5 && y < 5))
			return true;
		return false;
	case 6:
		if (x <= 4 || y <= 4 || (x < 6 && y < 6))
			return true;
		return false;
	default:
		return true;
	}
}

int main(int argc, char *argv[]) {
	uint64_t num;
	cin >> num;
	for (auto i = 0; i < num; i++) {
		uint64_t nom, x, y;
		cin >> nom >> x >> y;
		cout << "Case #" << i+1 << ": " << (assholeblock(nom, x, y) ? "RICHARD" : "GABRIEL") << endl;
	}
}