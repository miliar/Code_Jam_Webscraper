#include<iostream>
#include<fstream>
using namespace std;
int main() {
	ifstream in("D-small-attempt4.in");
	//ifstream in("smallD");
	int tc_count;
	in >> tc_count;
	for(int i = 0;i<tc_count;++i) {
		int X, R, C;
		in >> X >> R >> C;

		//cout << X << " " << R << " " << C << endl;
		//order R and C
		if(R > C) {
			swap(R,C); // C is now always > R
		}
		if(X >= 7) {
			//richard wins
			//can choose one with a hole in the middle
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		} else if(X == 1 && R == 1 && C == 1) {
			cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
		} else if(X > C) {
			//figure out if any of the N-ominos dont fit in one of the dimentions
			//L shape is most efficient for this
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		} else if(X >= 3 && C == 3 && R == 1) {
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		} else if(X >= 3 && C == 4 && R == 1) {
			cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		} else {
			//any piece will fit inside.. find out how many squares are left
			//see if we can fill them
			//can they make a T to split the area
			if(C == 4 && R == 2 && X == 4) {
					cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
			} else {

				int space = R * C;
				if(space % X == 0) {
					//we can fit them
					cout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;
				} else {
					cout << "Case #" << i + 1 << ": " << "RICHARD" << endl;

				}
			}

		}

	}
	return 0;
}
