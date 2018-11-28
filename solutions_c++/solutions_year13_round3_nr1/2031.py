// GoogleCodeJam_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <cstring>

#define MAX_N 100

using namespace std;

ifstream fin("D:\\Input.in");
ofstream fout("D:\\Output.txt");

int T, answer;

bool check_str(string str)
{
	for(int i = 0; i < str.length(); i++) if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u') return false;
	return true;
}

int main()
{
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		answer = 0;
		int n, L;
		string s;
		fin >> s >> n;
		L = s.length();
		for(int j = 0; j < L; j++)
		{
			for(int k = j; k < L; k++)
			{
				string strn = s.substr(j, k - j + 1);
				if(strn.length() < n) continue;
				for(int q = 0; q < strn.length(); q++)
				{
					if(strn.substr(q, n).length() != n) continue;
					if(check_str(strn.substr(q, n)))
					{
						answer++; goto next;
					}
				}
next:
				;
			}
		}
		fout << "Case #" << i + 1 << ": " << answer << "\n";
	}
	return 0;
}