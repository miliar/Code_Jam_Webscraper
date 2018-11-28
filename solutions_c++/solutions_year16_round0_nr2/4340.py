// codejam_RevengeOfPancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
	//fstream fin("B-small-attempt0.in", ios::in);
	//fstream fout("B-small-attempt0.out", ios::out);

	fstream fin("B-large.in", ios::in);
	fstream fout("B-large.out", ios::out);
	int T; fin >> T;

	for (int c = 0; c < T; c++) {
		string s; fin >> s;
		int count = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			if (s[i] == '-') {
				count++;
				for (int j = i; j >= 0; j--) {
					if(s[j] == '+')
						s[j] = '-';
					else
						s[j] = '+';
				}
			}
		}
		
		fout << "Case #" << c + 1 << ": " << count << endl;		
	}

	return 0;
}