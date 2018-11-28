#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;
	for (int test = 1; test <= T; test++) {
		out << "Case #" << test << ": ";
		string S;
		in >> S;
		S += '+';
		int ans = 0;
		for (int i = 0; i < (int)S.length() - 1; ++i) {
			ans += S[i] != S[i + 1];
		}
		out << ans << endl;
	}
	return 0;
}