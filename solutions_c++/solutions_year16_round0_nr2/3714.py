// PancakeRevenge.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;


int main()
{
	int t;
	cin >> t;

	for (int c = 1; c <= t; ++c) {
		string s;
		cin >> s;

		int result = 1;

		char curr = s[0];

		for (int i = 1; i < s.size(); ++i) {
			if (s[i] != curr) {
				++result;
				curr = s[i];
			}
		}

		if (s[s.size()-1] == '+') {
			--result;
		}

		cout << "Case #" << c << ": " << result << endl;
	}

    return 0;
}

