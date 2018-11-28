#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
using namespace std;


int main() {
	ifstream inp("A-large.in");
	ofstream outp("output.txt");
	int n;
	inp >> n;
	for (int i = 0; i < n; i++)
	{
		int start, inc;
		inp >> start;
		inc = start;
		if (start == 0) { outp << "Case #" << i + 1 << ": INSOMNIA" << endl; continue; }
		vector<bool> num(10, false);
		while (true)
		{
			string s = to_string(start);
			for (int j = 0; j < s.length(); j++)
				num[s[j] - '0'] = true;
			if (num[0] && num[1] && num[2] && num[3] && num[4] && num[5] && num[6] && num[7] && num[8] && num[9]) break;
			start += inc;
		}
		outp << "Case #" << i + 1 << ": " << start << endl;
	}
}