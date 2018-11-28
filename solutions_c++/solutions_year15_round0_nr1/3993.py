#include <fstream>
#include <iostream>
#include <string>


using namespace std;

int T, Smax;
string number;

ifstream in("A-large.in");
ofstream out("out.txt");

int main() {

	in >> T;
	for (int t = 1; t <= T; ++t) {
		in >> Smax >> number;

		int n = int(number.length());
		int already_stand_up = 0, people_added = 0;
		for (int i = 0; i < n; ++i) {
			if (already_stand_up < i) {
				people_added += i - already_stand_up;
				already_stand_up = i;
			}
			already_stand_up += number[i] - '0';
		}

		out << "Case #" << t << ": " << people_added << endl;

	}



	return 0;
}