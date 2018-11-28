#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");

	int t;
	string s;

	input >> t;

	for (int i = 1; i <= t;i++) {
		input >> s;
		int count = 0;


		for (int i = 0;i < s.size();i++) {
			if (s[i] == '-') {
				count = count + 2;
				for (i;i < s.size();i++)
					if (s[i] == '+') {
						break;
					}
			}
		}

		if (s[0] == '-')
			count--;

		output << "Case #" << i << ": " << count << endl;
	}
	return 0;
}