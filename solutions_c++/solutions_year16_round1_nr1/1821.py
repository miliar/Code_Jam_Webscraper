// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <functional>
#include <array>
#include <iostream>
#include <string>

using namespace std;

void Solve(int TID, string S)
{
	string R = "";
	R = R + S[0];
	char l = S[0];
	char r = S[0];

	for (int i = 1; i < S.length(); i++)
	{
		if (S[i] >= l) {
			R =  S[i] + R;
			l = S[i];
		}

		else
		{
			R = R + S[i];
			r = S[i];
		}
		
	}
	
	cout <<  "Case #" << TID << ": " << R << "\n";
}
int main()
{
	std::array<int, 10> tests = { 5, 7, 4, 2, 8, 6, 1, 9, 0, 3 };
	string input;

	unsigned long long int  T;
	scanf_s("%lld", &T); getline(cin, input);
	for (int i = 1; i <= T; i++)
	{
		unsigned long long int N;
		getline(cin, input);
		Solve(i, input);
	}	
    return 0;
}

