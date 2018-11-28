// codejam_A_CountingSheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>

using namespace std;

int main()
{
	fstream fin("A-large.in", ios::in);
	fstream fout("A-large.out", ios::out);
	int T; fin >> T;
	

	for (int t = 0; t < T; t++) {
		long long N; fin >> N;
		long long last = 0;
		bitset<10> bs;
		for (int i = 1; i <= 100; i++) {
			long long r = long long(N*i);
			while (r > 0) {
				bs[r % 10] = true;
				r /= 10;
			}

			if (bs.all()) {
				last = long long(N*i);
				break;
			}
		}

		if (bs.all()) 
			fout << "Case #" << t + 1 << ": " << last << endl;
		else
			fout << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
	}

    return 0;
}

