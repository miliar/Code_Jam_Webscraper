#include <iostream>
#include <fstream>
#include <cassert>
#include <string>
#include <bitset>
#include <map>
#include <cmath>

using namespace std;


int main(){

	//ifstream inFile("input.txt");
	//assert(inFile);
	ofstream outFile("output.txt");

	outFile << "Case #1:" << endl;

	int n = 16;

	string jamCoinBase = "1";
	map<string, int> jamCoins;
	int numCoins = 0;

	int endI;

	//This controls the size for checking divisors.  As it increases, the program will take longer and
	//check more, but when you only need 50,
	for (int h = 2; h < 6 && numCoins < 50; h++) {

		for (int i = 1; i < pow(2, 14) && numCoins < 50; i++) {
			//Create jamCoin
			endI = i;
			bitset<14> theSet(i);
			jamCoinBase.append(theSet.to_string());
			jamCoinBase.append("1");
			//cout << jamCoinBase << " ";
			bool validJamCoin = true;
			long long divisors[11]{ 0 };

			for (int j = 2; j <= 10 && validJamCoin; j++) {

				//Find value in base j
				long long convertedValue = 0;
				for (int k = 0, l = jamCoinBase.length() - 1; k < jamCoinBase.length() - 1; k++, l--) {
					if (jamCoinBase[k] == '1') {
						long double j2 = j;
						long double l2 = l;
						long long value = pow(j2, l2);
						convertedValue = convertedValue + value;
					}
				}

				//account for one in the zeroes place
				convertedValue++;

				long long divisor = 0;
				bool divisorFound = false;
				//Find divisors
				for (long long m = 2; m <= pow(10, h) && !divisorFound; m++) {
					if (convertedValue % m == 0) {
						divisorFound = true;
						divisors[j] = m;
					}
				}

				if (!divisorFound) {
					validJamCoin = false;
				}
			}
			if (validJamCoin) {
				numCoins++;
				outFile << jamCoinBase << " ";
				for (int i = 2; i <= 10; i++) {
					outFile << divisors[i] << " ";
				}
				outFile << endl;
			}

			jamCoinBase.clear();
			jamCoinBase.append("1");
		}
	}


	//inFile.close();
	outFile.close();

	return 0;
}