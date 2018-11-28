#include <iostream>
#include <string>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int plates, plate[1001], tallest_plate = 0;
		cin >> plates;
		for (int i = 0; i < plates; i++) {
			cin >> plate[i];
			if (plate[i] > tallest_plate)
				tallest_plate = plate[i];
		}

		int fastest_eating = tallest_plate;
		for (int height = tallest_plate - 1; height >= 2; height--) {
			int cuts = 0;
			for (int i = 0; i < plates; i++) {
				if (plate[i] <= height)
					continue;
				int j = plate[i] - height;
				cuts += (j / height);
				if (j % height > 0)
					cuts++;
			}
			if (cuts + height < fastest_eating)
				fastest_eating = cuts + height;
		}
		cout << "Case #" << cas << ": " << fastest_eating << endl;
	}
	return 0;
}
