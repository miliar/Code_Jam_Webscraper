// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctgmath>
#include <algorithm>
#include <iomanip>
#include <bitset>

using namespace std;

vector<unsigned long long> coins;
vector<unsigned long long> coinsDiv;
unsigned long long myPow(unsigned long long b, unsigned long long p) {
	unsigned long long res = 1;
	for (unsigned long long i = 0; i < p; ++i) {
		res *= b;
	}
	return res;
}

unsigned long long fromBasetoDec(unsigned long long bi, int base) {
	unsigned long long ret = 0;
	unsigned long i = 0;
	while (bi)
	{
		ret += ((unsigned long long )bi%2) * (unsigned long long)myPow(base, i++);
		bi /= 2;
	}

	return ret;
}

void decal(unsigned long long ul) {
	long i = 0;
	unsigned long long ull;
	do {
		unsigned long long ulDec = ul << ++i;
		ull = ul + ulDec;
		if ((ul & ulDec) == 0) {
			bool isNotPresent = (find(coins.begin(), coins.end(), ull) == coins.end());
			if (isNotPresent) {
				coins.push_back(ull);
				coinsDiv.push_back(ul);
			}

			//cout << (( ((unsigned long long)ull / ul) * ul) == ull )<< endl;
		}
	} while (ull < 4294967295);
}

int main()
{

	ofstream fout("out.txt");

	unsigned long long ul = 3;

	unsigned long long UL = 32767;

	while (ul <= UL)
	{
		decal(ul);

		ul += 2;
	}

	fout << "Case #1:" << endl;
	
	int counter = 0;
	for (unsigned long i = 0; i < coins.size(); i++) {
		unsigned long long currentCoin = coins[i];
		unsigned long long currentDiv = coinsDiv[i];
		unsigned long long limi = 2147483649;
		if ((limi & currentCoin) == limi && currentCoin < ((unsigned long long)4294967295) ) {
			if (counter++ == 500) {
				break;
			}
			else {

				fout << bitset<32>(currentCoin);

				for (int b = 2; b <= 10; ++b) {
					fout << " ";

					fout << fromBasetoDec(currentDiv, b);

				}

				cout << bitset<16>(currentDiv) << endl;;

				//cout << " " << currentCoin << " " << currentDiv << " " <<(currentCoin % currentDiv) << endl;
				fout << endl;
			}
		}
	}

    return 0;
}

