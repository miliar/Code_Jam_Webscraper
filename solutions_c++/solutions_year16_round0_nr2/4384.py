#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
using namespace std;


int main() {
	ifstream inp("B-large.in");
	ofstream outp("output.txt");
	int n;
	inp >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		inp >> s;
		int r = 0, c = 0;
		if (s[0] == '-')
		{
			r++, c++;
			while (c < s.length() && s[c] == '-') c++;
			if (c == s.length()) { outp << "Case #" << i + 1 << ": " << r << endl; continue; }
		}
		for (; c < s.length() - 1; c++)
			if (s[c] == '+' && s[c + 1] == '-') r += 2;
		outp << "Case #" << i + 1 << ": " << r << endl;
	}
}