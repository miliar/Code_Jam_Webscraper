//============================================================================
// Name        : FairAndSquare.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
using namespace std;

bool palindrome(string s)
{
	for (int i = 0; i < s.size() / 2; ++i)
	{
		if (s[i] != s[s.size() - i - 1])
			return false;
	}
	return true;
}

int main() {
	vector<int> palindromes;

	for (long long i = 0; i <= pow(10, 3); ++i)
	{
		stringstream ss1;
		ss1 << i;
		if (palindrome(ss1.str()))
		{
			stringstream ss2;
			ss2 << i * i;
			if (palindrome(ss2.str()))
			{
				palindromes.push_back(i * i);
				cout << i << ", " << i * i << endl;
			}
		}
	}
	//cout << "done" << endl;

	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		int A, B;
		cin >> A >> B;
		vector<int>::iterator iterA = lower_bound(palindromes.begin(), palindromes.end(), A);
		vector<int>::iterator iterB = lower_bound(palindromes.begin(), palindromes.end(), B);
		int belowA = iterA - palindromes.begin() - 1;
		int belowB = iterB - palindromes.begin();
		if (*iterB != B)
		{
			--belowB;
		}
		int total = belowB - belowA;
		cout << "Case #" << caseNum << ": " << total << endl;
	}
}
