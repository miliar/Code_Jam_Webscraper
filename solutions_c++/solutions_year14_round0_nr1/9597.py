#include <fstream>
#include <iostream>
#include <set>

using namespace std;


const int SIZE = 4;
int a[SIZE][SIZE];
int b[SIZE][SIZE];

int intersect(int x, int y) {
	set<int> s; 
	int count = 0;
	int ans = -1;
	for(int i = 0; i < SIZE; i++) {
		s.insert(a[x][i]);
		cerr << a[x][i] << " ";
	}

	for (int i = 0; i < SIZE; i++) {
		cerr << b[y][i] << " ";
		if (s.count(b[y][i])) {
			count++;
			ans = b[y][i];
		}
	}

	cerr << endl;

	if (count == 0) {
		return -1;
	}

	if (count == 1) {
		return ans;
	}

	return -2;


}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;	

	for (int t = 0; t < T; t++) {
		int guess1 = -1;
		int guess2 = -1;
		in >> guess1;
		for (int i = 0; i < SIZE; i++) {
			for (int j = 0; j < SIZE; j++) {
				in >> a[i][j];				
			}
		}

		in >> guess2;

		guess1--;
		guess2--;
		for (int i = 0; i < SIZE; i++) {
			for (int j = 0; j < SIZE; j++) {
				in >> b[i][j];				
			}
		}

		int ans = intersect(guess1, guess2);

		out << "Case #" << t + 1 << ": ";
		if (ans == -1) {
			out << "Volunteer cheated!";
		} else if (ans == -2) {
			out << "Bad magician!";
		} else {
			out << ans;
		}
		out << endl;
	}
	return 0;
}
