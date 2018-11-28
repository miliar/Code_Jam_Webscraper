#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

	ifstream in("input.txt");
	ofstream out("output.txt");

int solve(){

	int smax;
	string s;
	in >> smax;
	in >> s;

	int all = 0;
	int exist = 0;
	for (int i = 0; i < s.length(); ++i) {
		int cur = s[i] - '0';
		all += max(0, i - all);
		all += cur;
		exist += cur;
	}

	return all - exist;

}

int main() {



	int T;
	in >> T;

	for (int i = 1; i <= T; ++i) {
		out << "Case #" << i << ": " << solve() << "\n";
	}

	return 0;
}