// revertPancake.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int flipHelper(string s) {
	int len = s.length();
	vector<int> optUp(len, 0);
	vector<int> optDown(len, 0);
	if (len == 0)
		return 0;
	if (s[0] == '+')
		optDown[0] = 1;
	else
		optUp[0] = 1;
	for (int i = 1; i < len; i ++) {
		if (s[i] == '+') {
			optUp[i] = optUp[i-1];
			optDown[i] = optUp[i-1] + 1;
		} else {
			optUp[i] = optDown[i-1] + 1;
			optDown[i] = optDown[i-1];
		}
	}
	return optUp[len-1];
}
int main()
{
	int T;
	string str;
	ifstream in;
	in.open("./B-large.in");
	ofstream out;
	out.open("./B-large.out");
	in >> T;
	for (int i = 0; i < T; i ++) {
		in >> str;
		out << "Case #" << i+1 << ": " << flipHelper(str) << endl;
	}
	in.close();
	out.close();
	return 0;
}


