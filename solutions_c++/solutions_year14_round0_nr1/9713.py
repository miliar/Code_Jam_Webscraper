#include<iostream>
#include<fstream>

using namespace std;

int main() {
	ifstream is;
	ofstream os;
	is.open("A-small-attempt0.in");
	os.open("op.txt");

	int T, A, B[20] = {0}, ans, num;

	is >> T;

	for(int i = 0; i < T; i++) {
		int count = 0;
		is >> A;
		for(int j = 0; j < 16; j++) {
			is >> num;
			if(j / 4 == A - 1) {
				B[num] = 1;
			}
		}

		is >> A;
		for(int j = 0; j < 16; j++) {
			is >> num;
			if(j / 4 == A - 1 && B[num]) {
				ans = num;
			    count++;
			}
		}

		if(count == 0) {
			os << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		} else if(count == 1) {
			os << "Case #" << i + 1 << ": " << ans << endl;
		} else {
			os << "Case #" << i + 1 << ": Bad magician!" << endl;
		}

		memset(B, 0, sizeof(B));

	}

	is.close();
	os.close();

	return 0;
}