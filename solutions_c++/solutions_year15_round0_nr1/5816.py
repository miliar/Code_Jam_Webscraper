#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("answerAlarge.txt");
	int t;
	in >> t;
	for (int ti = 1; ti <= t; ti++) {
		int smax;
		in >> smax;
		string aud;
		in >> aud;
		int cur_standing = 0;
		int needed = 0;
		//vector<int> shy;
		for (int i = 0; i < smax + 1; i++) {
			if (i <= cur_standing) {
				cur_standing += (int) (aud[i] - '0');
			} else {
				int new_needed = i - cur_standing;
				needed += new_needed;
				cur_standing += (int) (aud[i] - '0') + new_needed;
			}
		}
		out << "Case #" << ti << ": " << needed << endl;
	}
	return 0;
}
