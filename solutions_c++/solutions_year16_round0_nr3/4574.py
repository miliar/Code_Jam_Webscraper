// Shintero
// Problem C. Coin Jam - small
#include <iostream>
#include <cstdio>
#include <string>
#include <bitset>
#include <cmath>
#include<vector>
using namespace std;

long long numberOfTests, coinLength, numberOfCoins, currentCoin;

long long isPrime(long long number) {
	long long root = (long long)(sqrt(number));
	
	for (long long i = 2; i <= root; i++) {
		if (number % i == 0) {
			return i;
		}
	}
	
	return 0;
}

long long changeBaseTo(string number, long long base) {
	long long res = 0, pow = 1;
	long long len = number.length();
	
	for(int i = len - 1; i >= 0; i--) {
		if (number[i] == '1') {
			res += pow;
		}
		pow *= base;
	}
	
	return res;
}

string coinToString(long long number) {
	string res = "";
			
	while(number > 0 ) {
		if(number % 2 == 0) {
			res = "0" + res;
		}
		else {
			res = "1" + res;
		}
		number /= 2;
	}
	return res;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	cin >> numberOfTests;
	cin >> coinLength >> numberOfCoins;
	
	currentCoin = (2 << (coinLength - 2)) + 1;
	for(int k = 1; k <= numberOfTests; k++){
	cout << "Case #" << k << ":\n";
	while (numberOfCoins > 0) {
		vector<long long> divs;
		divs.clear();
		long long aux = currentCoin;
		
		if (aux % 2 == 0) {
			currentCoin++;
		}
		else{
			string auxString = coinToString(aux);
			
			for (long long i = 2; i <= 10; i++) {
				long long aux2 = changeBaseTo(auxString, i);
				long long aux3 = isPrime(aux2);
				
				if(aux3 == 0) {
					currentCoin++;
					break;
				}
				else {
					divs.push_back(aux3);
				}
			}
		
			if (divs.size() == 9) {
				cout << auxString << " ";
			
				for (long long j = 0; j < 8; j++) {
					cout << divs[j] << " ";
				}
				
				cout << divs[8] << "\n";
			
				numberOfCoins--;
				currentCoin++;
			}
		}
	}
}
	return 0;
}
