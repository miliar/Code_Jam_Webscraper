#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int t, sMax, ans, num;
string s;

int main() {
	ifstream ifs("C:\\Users\\Admin\\Desktop\\A-large.in");
	ofstream ofs("output.out");

	ifs >> t;

	for (int i = 1; i <= t; ++i) {
		
		ifs>>sMax;

		ifs >> s;

		ans = 0; num = 0;

		for (int j = 0; j < s.size(); ++j) {
			if (j <= num)
				num += s[j] - '0';
			else {
				ans += j - num;
				num += s[j] - '0' + j - num;
			}
		}

		ofs << "Case #" << i << ": " << ans << endl;

	}

	return 0;
}