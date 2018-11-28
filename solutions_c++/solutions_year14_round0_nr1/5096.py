#include <iostream>
#include <fstream>
using namespace std;

void main() {
	ifstream in1;
	in1.open("A-small-attempt2.in");
	ofstream out1;
	out1.open("out.txt");

	int T;
	int c1, c2;
	int arr1 [16];
	int arr2 [16]; 
	int poss [4];
	int result;
	bool found = false;
	bool found1 = false;
	in1 >> T;
	
	for (int i = 0; i < T; i++) {
		found = false;
		found1 = false;
		in1 >> c1;
		for (int j = 0; j < 16; j++) {
			in1 >> arr1[j];
		}
		for (int k = 0; k < 4; k++)
			poss[k] = arr1[(c1-1)*4 + k];
		in1 >> c2;
		for (int m = 0; m < 16; m++)
			in1 >> arr2[m];
		for (int l = 0; l < 4; l++) {
			for (int n = 0; n < 4; n++) {
				if (!found && poss[l] == arr2[(c2-1)*4 + n]) {
					found = true;
					result = poss[l];
				}
				else if (found && poss[l] == arr2[(c2-1)*4 + n])
					found1 = true;
			}
		}
		if (found1) {
			out1 << "Case #" << i+1 << ": Bad magician!" << endl;
		}
		else if (found)
			out1 << "Case #" << i+1 << ": " << result << endl;
		else
			out1 << "Case #" << i+1 << ": Volunteer cheated!" << endl;
	}
	in1.close();
	out1.close();
}