// codejam_C_CoinJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

long long isPrime(long long num) {
	for (long long i = 2; i <= sqrt(num); i++) {
		if (num%i == 0)
			return i;
	}

	return 0;
}

int main()
{
	fstream fout("c.out", ios::out);
	fout << "Case #1:" << endl;
	int T = 1;
	for (int c = 1; c <= T; c++) {
		int N = 6;
		int found = 0;
		long long base_bits = 32769;
		//long long base_bits = 33;
		

		while (found < 50) {
			long long result = 0;
			long long t = base_bits;
			vector<string> divs;
			
			bool jam = true;
			for (int i = 2; i <= 10; i++) {
				int a = 0;
				while (t > 0) {
					result += (t & 1) * pow(i, a);
					a++;
					t >>= 1;
				}

				t = base_bits;

				long long d = isPrime(result);
				if (d == 0) {
					jam = false;
					break;
				}
				else 
					divs.push_back(to_string(d));

				result = 0;
			}

			if (jam) {
				string jamnum = "";

				long long k = base_bits;
				while (k > 0) {
					jamnum = to_string(k&1) + jamnum;
					k >>= 1;
				}

				fout << jamnum << " ";
				for (int i = 0; i < divs.size(); i++) 
					fout << divs[i] << " ";
				fout << endl;
				found++;
			}

			base_bits += 2;
		}
	}


    return 0;
}

