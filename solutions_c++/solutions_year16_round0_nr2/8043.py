// Problem B. Revenge of the Pancakes.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstring>

short int const N = 100;

using namespace std;


void main()
{
	ofstream fout("output.out");
	ifstream fin("B-large.in");
	int n;
	fin >> n;
	char s[N + 1];
	for (int t = 1;t <=n ;t++) {
		char s[N + 1];
		fin >> s;
		if (!s[1]) {
			if (s[0] == '-') fout << "Case #" << t << ": " << 1<<endl;
			else fout << "Case #" << t << ": " << 0<<endl;
			continue;
		}
		int k = 0;
		int i = 1;
		for (; s[i] ;i++)
			if (s[i] != s[i - 1]) k++;
		if (s[i - 1] == '-') k++;
		fout << "Case #" << t << ": " << k<<endl;
	}
}

