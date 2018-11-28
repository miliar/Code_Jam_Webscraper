#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	int a1, a2;
	int r1[4], r2[4];
	int T, t;
	ofstream fileoutput;
	ifstream fileinput;
	fileoutput.open("output.txt");
	fileinput.open("input.txt");
	if (fileinput.is_open()) {
		cout << "here";
	}

	int ca = 0;
	fileinput >> T;

	while (ca < T) {
		fileinput >> a1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == a1 - 1) {
					fileinput >> r1[j];
				}
				else {
					fileinput >> t;
				}
			}
		}

		fileinput >> a2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (i == a2 - 1) {
					fileinput >> r2[j];
				}
				else {
					fileinput >> t;
				}
			}
		}

		int cnt = 0;
		int theone = -1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (r1[i] == r2[j]) {
					theone = r1[i];
					cnt++;
				}
			}
		}

		ca++;
		//cout << "Case #" << ca << ": ";
		fileoutput << "Case #" << ca << ": ";
		if (cnt == 0) {
			//cout << "Volunteer cheated!" << endl;
			fileoutput << "Volunteer cheated!" << endl;
		}
		if (cnt == 1) {
			//cout << theone << endl;
			fileoutput << theone << endl;
		}
		if (cnt > 1) {
			//cout << "Bad magician!" << endl;
			fileoutput << "Bad magician!" << endl;
		}


	}
	return 0;
}