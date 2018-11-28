#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("outA.txt");

	int T;
	in >> T;
	for (int i = 1; i <=T; i++) {
		int Smax;
		in >> Smax;
		string s;
		in >> s;
		const char *str = s.c_str();
		int sum = str[0] - '0';
		int y = 0;
		for (int j = 1; j <= Smax; j++) {
			if (sum < j) {
				y += j - sum;
				sum += j - sum;
			}
			sum += str[j] - '0';
		}
		out << "Case #" << i << ": " << y << endl;
	}

	return 0;
}