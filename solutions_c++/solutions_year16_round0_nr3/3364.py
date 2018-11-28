// ConsoleApplication4.cpp : Defines the entry polong long for the console application.
//

#include "stdafx.h"

#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<vector>

using namespace std;
long long tobase(string coin, long long k);
long long isprime(long long n);
string makecoin(long long j, long long length);

vector <long long> primes;

int main() {
	long long numIn;
	ifstream ifs;
	ifs.open("c.txt");
	ifs >> numIn;
	ofstream ofs;
	ofs.open("clarge.txt");
	primes.push_back(2);

	for (long long i = 0; i < numIn; i++) {
		long long length, numCoins;
		ifs >> length;
		ifs >> numCoins;
		ofs << "Case #" << i + 1 << ": " << endl;
		//cout << length << endl;
		//cout << numCoins << endl;
		long long middleLength = length - 2;
		long long coinsSoFar = 0;
		for (long long j = 0; j < pow(2, middleLength); j++) {
			string coin = makecoin(j, length);
			bool isacoin = true;
			long long divs[9];

			for (long long k = 2; k <= 10; k++) {
				long long coin_num = tobase(coin, k);
				     //cout << "\t" << coin << " in base "<<k<<" is "<< coin_num << endl;
				long long div = isprime(coin_num);

				if (div == 0) {
					//not a jamcoin
					isacoin = false;
					break;
				}
				divs[k - 2] = div;
			}
			if (isacoin) {
				coinsSoFar++;
				cout << coinsSoFar;
				ofs << coin;
				for (long long k = 0; k < 9; k++)
					ofs << " " << divs[k];
				ofs << endl;
				if (coinsSoFar >= numCoins)
					break;
			}
		}

	}

}

long long isprime(long long n) {
	//for (long long i = 0; i < primes.size() && primes[i]*primes[i] <= n; i++)
	for(long long i = 2; i*i < n; i++)
		if (n % i == 0)
			return i;
	//primes.push_back(n);
	return 0; // returns 0 if prime

}

long long tobase(string coin, long long k) {
	long long ret = 0;
	for (int i = coin.length() - 1; i >= 0; i--) {
		if (coin[i] == '1')
			ret += pow(k, (coin.length() - 1 - i));
	}
	return ret;
}

//long long makecoin(long long j, long long length){
//return 1 + 2*j + pow(2, length-1);
//}

string makecoin(long long j, long long length) {
	string ret = "";
	for (long long i = 0; i < length - 2; i++) {
		if (j % 2 == 1)
			ret = ret + "1";
		else
			ret = ret + "0";
		j = j / 2;
	}
	return "1" + ret + "1";
}
