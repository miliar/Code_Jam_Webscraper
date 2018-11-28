// round0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

bool ispalindrome(int x)
{
	stringstream ss;
	ss << x;
	string s = ss.str();
	int len = s.length();
	for (int i = 0; i < len / 2; i++)
		if (s[i] != s[len-1-i]) return false;
	return true;
}

int fair_and_square(int A, int B)
{
	int ans = 0;
	int s = sqrt((double)A);
	int e = sqrt((double)B);
	for (int i = s; i <= e; i++)
	{
		int sq = i * i;
		if (sq < A || sq > B) continue;
		if (ispalindrome(sq) && ispalindrome(i)) ans++;
	}
	return ans;
}

int main(int argc, char* argv[])
{
	ifstream in("C-small-attempt1.in");
	ofstream out("output.txt");
	string line;

	getline(in, line);
	int T = atoi(line.c_str());
	for (int i = 0; i < T; i++)
	{
		getline(in, line);
		int pos = line.find(' ');
		int A = atoi(line.substr(0, pos).c_str());
		int B = atoi(line.substr(pos+1).c_str());
		out << "Case #" << i+1 << ": " << fair_and_square(A, B) << endl;
	}
	return 0;
}