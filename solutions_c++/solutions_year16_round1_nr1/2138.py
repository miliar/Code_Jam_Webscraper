// lastword.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"
using namespace std;

void computeLastWord(string str);
int findIndexLastMaxChar(string str, int length);

int main()
{
	int t;
	string str;

	cin >> t;

	getline(cin, str); // read until end of line (needed if getline is used)

	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";

		getline(cin, str);

		computeLastWord(str);

		cout << "\n";
	}

	return 0;
}

void computeLastWord(string str)
{
	string newStr;

	string front = "";
	string back = "";
	int maxCharIndex;

	int unprocessLen = str.length();

	if (str.length() == 0) {
		return;
	}

	while (unprocessLen > 0)
	{
		maxCharIndex = findIndexLastMaxChar(str, unprocessLen);
		front += str[maxCharIndex];
		back.insert(0, str.substr(maxCharIndex + 1, unprocessLen - maxCharIndex - 1));

		unprocessLen = maxCharIndex;
	}
	
	newStr = front.append(back);

	cout << newStr;
}


int findIndexLastMaxChar(string str, int length)
{
	int indexMax = 0;
	for (int i = 1; i < length; i++) {
		if (str[i] >= str[indexMax]) {
			indexMax = i;
		}
	}

	return indexMax;
}