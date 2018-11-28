#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int caseNum = 1; caseNum <= t; caseNum++) {
		string s;
		cin >> s;
		stringstream ss;
		ss << s[0];
		string winningword;
		ss >> winningword;
		for(int i = 1; i < s.length(); i++) {
			if(s[i] < winningword[0])
				winningword += s[i];
			else
				winningword = s[i] + winningword;
		}
		cout << "Case #" << caseNum << ": " << winningword << endl;
	}
	return 0;
}