#include<iostream>
#include<fstream>

using namespace std;

int main() {
	int count;
	int row;
	int col;

	int arr[16];

	int tmp0[4];
	int tmp1[4];

	int res = 0;

	ifstream input ("input.txt");
	ofstream output ("output.txt");

	input >> count;

	for (int i = 0; i < count; ++i) {
		res = 0;

		input >> row;
		
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				input >> arr[k + j * 4];
			}
		}

		tmp0[0] = arr[(row - 1) * 4];
		tmp0[1] = arr[(row - 1) * 4 + 1];
		tmp0[2] = arr[(row - 1) * 4 + 2];
		tmp0[3] = arr[(row - 1) * 4 + 3];

		input >> row;

		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				input >> arr[k + j * 4];
			}
		}

		tmp1[0] = arr[(row - 1) * 4];
		tmp1[1] = arr[(row - 1) * 4 + 1];
		tmp1[2] = arr[(row - 1) * 4 + 2];
		tmp1[3] = arr[(row - 1) * 4 + 3];

		for (int j = 0; j < 4; ++j) {
			cout << tmp0[j] << endl;
		}

		for (int j = 0; j < 4; ++j) {
			cout << tmp1[j] << endl;
		}

		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (res != -1) {
					if (tmp0[j] == tmp1[k]) {
						if (res == 0) {
							res = tmp0[j];
						}
						else {
							res = -1;
						}
					}
					else {

					}
				}
			}
		}

		output << "Case #" << (i + 1) << ": ";

		if (res == -1) {
			output << "Bad magician!" << endl;
		}
		else if (res == 0) {
			output << "Volunteer cheated!" << endl;
		}
		else {
			output << res << endl;
		}
	}
	
	return 0;
}