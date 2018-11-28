#include <iostream> 
#include <fstream>
using namespace std;

int main() {
	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");
	int n;
	in >> n;
	int arr[4][4];
	int arr2[4][4];
	for (int k = 0; k < n; k++) {
		int row;
		in >> row;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				in >> arr[i][j];

		int row2;
		in >> row2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				in >> arr2[i][j];

		int kol = 0, res = 0;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (arr[row - 1][i] == arr2[row2 - 1][j]) {
					res = arr[row - 1][i];
					kol++;
				}
			}
		}
		out << "Case #" << k + 1 << ": ";
		if (kol == 1)
			out << res << endl;
		else {
			if (kol > 1)
				out << "Bad magician!" << endl;
			else
				out << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}