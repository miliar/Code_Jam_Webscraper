#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "Usage: solver <input-file>" << endl;
		cerr << "Wrong number of arguments!" << endl;
		return 1;
	}
	ifstream inputFile;
	inputFile.open(argv[1], ifstream::in);
	if (!inputFile.is_open()) {
		cerr << "Could not open '" << argv[1] << "'." << endl;
		return 1;
	}
	int T;
	inputFile >> T;
	//cout << "Processing " << T << " cases:" << endl;
	int map[100][100];
	bool checked[100][100];
	for (int t = 1; t <= T; t++) {
		int X, Y;
		inputFile >> Y >> X;
		for (int y = 0; y < Y; y++) {
			for (int x = 0; x < X; x++) {
				inputFile >> map[x][y];
				//cout << map[x][y] << " ";
				checked[x][y] = false;
			}
			//cout << endl;
		}
		if (Y == 1 || X == 1) {
			// Haha, piece of cake :P
			cout << "Case #" << t << ": YES" << endl;
			continue;
		}
		for (int y = 0; y < Y; y++) {
			for (int x = 0; x < X; x++) {
				// If not checked before
				if (checked[x][y]) continue;
				// See if it can be cut horizontally
				bool ok = true;
				for (int i = 0; i < X; i++) {
					if (map[i][y] > map[x][y]) {
						ok = false;
						break;
					}
				}
				if (ok) {
					checked[x][y] = true;
					// Also, all other same high grass can be cut this way
					for (int i = 0; i < X; i++) {
						if (map[i][y] == map[x][y]) {
							checked[i][y] = true;
						}
					}
					continue;
				}
				// See with vertical cutting
				ok = true;
				for (int i = 0; i < Y; i++) {
					if (map[x][i] > map[x][y]) {
						ok = false;
						break;
					}
				}
				if (ok) {
					checked[x][y] = true;
					// Also, all other same high grass can be cut this way
					for (int i = 0; i < X; i++) {
						if (map[x][i] == map[x][y]) {
							checked[x][i] = true;
						}
					}
					continue;
				}
				// Ohh oh, problem here
				//cout << "Problem: " << x << ", " << y << endl;
				goto testFailed;
			}
		}
		cout << "Case #" << t << ": YES" << endl;
		continue;
testFailed:
		cout << "Case #" << t << ": NO" << endl;
	}
}
