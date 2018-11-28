#include <iostream>
#include <fstream>
#include <set>
#include <string>
using namespace std;

int main() {
	ifstream in("A-small-attempt0.in");
	ofstream out("Output.txt");
	int T;
	in >> T;
	int array[4][4];
	for (int n=0; n<T; ++n) {
		set<int> s;
		int pos;
		in >> pos;
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				in >> array[i][j];
				if (i+1 == pos) {
					s.insert(array[i][j]);
				}
			}
		}
		in >> pos;
		int count = 0, value = 0;
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				in >> array[i][j];
				if (i+1 == pos) {
					if (s.insert(array[i][j]).second == false) {
						++count;
						value = array[i][j];
					}
				}
			}
		}
		if (count == 0) {
			out<<"Case #"<<n+1<<": Volunteer cheated!"<<endl;
		} else if (count > 1) {
			out<<"Case #"<<n+1<<": Bad magician!"<<endl;
		} else {
			out<<"Case #"<<n+1<<": "<<value<<endl;
		}
	}
	return 0;
}