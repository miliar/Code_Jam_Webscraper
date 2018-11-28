#include <fstream>
#include <string>

using namespace std;

int T;
string p;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;

	for(int t = 1; t <= T; t++) {
		out << "Case #" << t << ": ";
		in >> p;

		int flips = 0;
		bool up = false;

		for(int i = p.length()-1; i >= 0; i--) {
			if((p.at(i) == '+') == up) {
				flips++;
				up = !up;
			}
		}

		out << flips << endl;
	}

	return 0;
}
