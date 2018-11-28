#include "C.h"

#include <cassert>
#include <iostream>
#include <string>
#include <numeric> 
#include <vector> 
#include <sstream>
#include <math.h> 

using namespace std;

string DecToBin(unsigned long long number);
int getRealDiv(string jamcoin, int base);

void solveC(){
	FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("C-small-attempt0.out", "w", stdout);
	int T;

	cin >> T;
	for (int t = 1; t <= T; t++){
		int n, j;
		int done = 0;
		cin >> n >> j;


		cout << "Case #" << t << ": "<<endl;
		
		unsigned long long num = pow(2, n - 1) + 1;
		unsigned long long max = pow(2, n) - 1;
		do{
			string jamCoin = DecToBin(num);
			num += 2;
			//string jamCoin = "111001";

			int divs[9] = { 0 };
			int div = 0;
			for (int i = 0; i < 9; i++){
				div = getRealDiv(jamCoin, i + 2);
				if (div == 0){
					break;
				}
				divs[i] = div;
			}
			if (div == 0){
				continue;
			}
			cout << jamCoin;
			for (int i = 0; i < 9; i++){
				cout << " " << divs[i];
			}
			cout << endl;
			done++;
			
		} while (done != j&&(num-2)<max);
		
		

	}
}

string DecToBin(unsigned long long number)
{
	if (number == 0) return "0";
	if (number == 1) return "1";

	if (number % 2 == 0)
		return DecToBin(number / 2) + "0";
	else
		return DecToBin(number / 2) + "1";
}

int getRealDiv(string jamcoin, int base){

	unsigned long long number = 0;
	
	for (int i = 0; i < jamcoin.size(); i++){
		if (jamcoin.at(i) == '1'){
			number += pow(base, jamcoin.size() - i-1);
		}
	}

	if (number <= 1)
		return 0;
	else if (number == 2)
		return 0;
	else if (number % 2 == 0)
		return 2;
	else
	{
		
		int divisor = 3;
		double num_d = static_cast<double>(number);
		int upperLimit = static_cast<int>(sqrt(num_d) + 1);

		while (divisor <= upperLimit)
		{
			if (number % divisor == 0){
				return divisor;
			}
			divisor += 2;
		}
		return 0;
	}
}
