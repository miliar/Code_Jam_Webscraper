#include <fstream>
#include <string>

using namespace std;

ifstream in("input");
ofstream out("output");

int main() {

	int T;
	in >> T;

	for(int t = 1; t <= T; ++t) { 
		int n;
		in >> n;

		string shy;
		in >> shy;

		int total_standing = 0;

		int to_add = 0;

		for(int i = 0; i <= n; ++i) {
			if(shy[i] == '0') continue;

			if(total_standing < i) {
				to_add += i - total_standing;
				total_standing += i - total_standing;
			}
			total_standing += shy[i]-'0';
		}

		out << "Case #" << t << ": " << to_add << '\n';
	}
}