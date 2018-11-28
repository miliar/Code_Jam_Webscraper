#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <algorithm>


using namespace std;

int main(int argc, char* argv[])
{
	std::ifstream infile("infile.txt");
	std::ofstream outfile("outfile.txt");

	int T = 0;
	infile >> T;

	for (int j = 1; j <= T; ++j) {
		string s;
		infile >> s;

		string t;
		t += s[0];
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] >= t[0]) {
				t = s[i] + t;
			}
			else {
				t += s[i];
			}
		}

		outfile << "Case #" << j << ": " << t << std::endl;
	}

	return 0;
}
