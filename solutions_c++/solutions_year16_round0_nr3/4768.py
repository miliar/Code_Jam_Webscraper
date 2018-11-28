// ConsoleApplication5.cpp : Defines the entry point for the console application.
#include <iostream>
#include <conio.h>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <iterator>

using namespace std;
set <long long int> primes;

long long int dec_to_bin(int i)
{
	long long int b = 0, pos = 0, remainder;
	while (i>0)
	{
		remainder = i % 2;
		b += remainder*pow(10, pos++);
		i /= 2;
	}
	return b;
}



bool isPrime( long long int num) {

	if (primes.find(num) != primes.end()) {
	
		return true;
	}
	int flag = 0;
	long long int i = 2;
	for (i = 2; i <= sqrt(num); ++i)
	{
		if (num%i == 0)
		{		
			flag = 1;
			break;
		}
	}

	if (flag == 0) {

		primes.insert(num);
		return true;
	}
	else
		return false;

}
int main() {
	int T = 1, N = 16, J = 50;

	ofstream outfile;
	string line;
	outfile.open("D:/GoogleCodeJam/coinJamSmall.txt");

	outfile << "Case #1:" << endl;
	
	int j_count = 0;
	int maxNum = pow(2, N-2);
	for (int i = 0; i < maxNum; i++) {
		if (j_count == J){
			cout << "Done" << endl;
			break;
		}

		long long int binNum = dec_to_bin(i);
		vector<int> jamCoin;	
		jamCoin.push_back(1);
		for (int j = 1; j < N -1; j++){
			jamCoin.push_back(0);
		}
		jamCoin.push_back(1);
		int end = N - 2;
		while (binNum) {
			jamCoin[end] = binNum % 10;
			binNum = binNum / 10;
			end--;
		}

		std::reverse(jamCoin.begin(), jamCoin.end());
		long long int baseEquivalent[9] = { 0 };
		long long int nonTrivialFactor[9] = { 0 };

		for (int b = 0; b < 9; b++) {

			long long int baseEquiNum = 0;
			for (int j = 0; j < N; j++) { 
				baseEquiNum += jamCoin[j]*pow(b+2, j); 
			}

			if (isPrime(baseEquiNum)) {	 				
				break;
			}
			baseEquivalent[b] = baseEquiNum;
				  
		}


		bool proceed = true;
		for (int b = 0; b < 9; b++) {
			if (baseEquivalent[b] == 0) {
				proceed = false;
				break;
			}
		}

		if (proceed) {
			
			string factorStr = "";
			for (int b = 0; b < 9; b++) {
				ostringstream Convert;
				long long int i = 2;
				while (i) {
					if (baseEquivalent[b] % i == 0) {
						nonTrivialFactor[b] = baseEquivalent[b] / i;
						Convert << i;
						factorStr += " "+ Convert.str();
						break;
					}
					i++;
				}
				
			}

			j_count++;
			if (!factorStr.empty()) {
				std::reverse(jamCoin.begin(), jamCoin.end());
				for (int j = 0; j < N; j++){
					outfile << jamCoin[j];
				}
				
				outfile << factorStr << endl;
			}

		}




	}

	outfile.close();
	_getch();
}