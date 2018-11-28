// LastWord.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";

		string s;
		cin >> s;

		string result;
		result += s[0];

		for (int j = 1; j < s.size(); ++j) {
			if (s[j] >= result[0]) {
				result = s[j] + result;
			}
			else {
				result += s[j];
			}
		}

		cout << result << endl;

	}
    return 0;
}

