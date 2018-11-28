#include <iostream>  
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>
#include <iterator>

using namespace std;
struct S {
	int cnt; string p; S(int a, string b) { cnt = a; p = b; };
};
	static bool sorter(S b, S a) {
		if (a.cnt < b.cnt) return true;
		return false;
	}
	string Senate(vector<S> w) {
		string ret = "";
		
		int sz = w.size();
		int tot = 0;
		for (int n = 0; n < sz; n++) tot += w[n].cnt;
		sort(w.begin(), w.end(), sorter);
		bool first = true;
		while (tot > 0) {
			sort(w.begin(), w.end(), sorter);
			if (!first) ret += " ";
			first = false;
			if (tot - 1 < w[1].cnt * 2) {
				ret += (w[0].p + w[1].p);
				tot -= 2;
				w[0].cnt--;
				w[1].cnt--;
			}
			else {
				w[0].cnt--;
				tot--;
				ret += w[0].p;
			}

		}
		return ret;
	}

	void main() {

		//	ifstream infile("2016R1\\C\\A-small-attempt0.in");
		//	ofstream outfile("2016R1\\C\\A-small-attempt0.out");
			ifstream infile("2016R1\\C\\A-large.in");
			ofstream outfile("2016R1\\C\\A-large.out");

		//ifstream infile("2016R1\\C\\sample.in");
		//ofstream outfile("2016R1\\C\\sample.out");

		int cnt;
		infile >> cnt;

		for (int n = 1; n <= cnt; n++) {
			int rows;
			infile >> rows;
			vector<S> nums;

			for (int m = 0; m < rows; m++) {
				stringstream ss;
				string s;
				int num;
				infile >> num;
				char o = static_cast<char>('A' + m);
				ss << o;
				ss >> s;
				nums.push_back(S(num, s));
			}

			string ret = Senate(nums);

			outfile << "Case #" + to_string(n) + ": " + ret << "\n";
		}
	}

