#include <iostream>
using namespace std;

int main(void) {
	int numCases;

	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int R, C, W;

		cin >> R >> C >> W;
		cout << "Case #" << numCase << ": " << R * (int)(C / W) + (C % W ? W : W - 1) << endl;
	}
}