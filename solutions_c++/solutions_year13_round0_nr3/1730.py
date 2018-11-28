// GoogleCodeJam_Palindromes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>

#define MAX_N 10000000

using namespace std;

ifstream fin("D:\\Input.in");
ofstream fout("D:\\Output.txt");

int T;
long long storepals[MAX_N], counteri;

bool palindrome(string stringtest)
{
	int stringlength = stringtest.length();
	for(int i = 0; i < stringlength; i++) if(stringtest[i] != stringtest[stringlength - i - 1]) return false;
	return true;
}

void generate(long long n)
{
	for(long long i = 1; i <= n; i++)
	{
		string str = to_string(i);
		string str2 = to_string(i*i);
		if(palindrome(str) && palindrome(str2)) {storepals[counteri++] = i*i;}
	}
}

int main()
{
	generate(10000000);
	fin >> T;
	for(int j = 0; j < T; j++)
	{
		int finalanswer = 0;
		long long A, B; fin >> A >> B;
		for(int k = 0; k < counteri; k++)
		{
			if(storepals[k] < A || storepals[k] > B) continue;
			finalanswer++;
		}
		fout << "Case #" << j + 1 << ": " << finalanswer << "\n";
	}
	return 0;
}