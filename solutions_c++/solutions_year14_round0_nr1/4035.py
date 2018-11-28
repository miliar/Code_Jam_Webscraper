#include <fstream>
#include <vector>

using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("out.txt");

void readCase(int &row1, int arr1[][4], int &row2, int arr2[][4]) {
	fin >> row1;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			fin >> arr1[i][j];
		}
	}
	fin >> row2;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			fin >> arr2[i][j];
		}
	}
}

void output(vector <int> answer) {
	for (int i = 0; i < answer.size(); i++) {
		fout << "Case #" << i + 1 << ": ";
		if (answer[i] == 0) {
			fout << "Volunteer cheated!" << endl;
		} else if (answer[i] == 17) {
			fout << "Bad magician!" << endl;
		} else {
			fout << answer[i] << endl;
		}
	}
}

int trick(int row1, int arr1[][4], int row2, int arr2[][4]) {
	int numbers[4];
	for (int i = 0; i < 4; i++) {
		numbers[i] = arr1[row1 - 1][i];
	}
	int res = 0, count = 0;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (arr2[row2 - 1][j] == numbers[i]) {
				res = numbers[i];
				count++;
			}
		}
	}
	if (count > 1) {
		return 17;
	} else return res;
}

int main() {
	int cases = 0;
	vector <int> res;
	fin >> cases;
	for (int i = 0; i < cases; i++) {
		int row1 = 0, row2 = 0;
		int arr1[4][4], arr2[4][4];
		readCase(row1, arr1, row2, arr2);
		res.push_back(trick(row1, arr1, row2, arr2));
	}
	output(res);
	return 0;
}