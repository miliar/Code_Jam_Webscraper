// Coin Jam.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#define MAXLEN 32
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <fstream>
using namespace std;

bool tryNextStr(char* num, int length){
	if (!num || length == 0){
		return false;
	}

	int cur = length - 2;
	
	int carryBit = 0;
	for (; cur >= 1; cur--){
		int curbit = num[cur] - '0' + carryBit;
		if (cur == length - 2){
			curbit++;
		}

		if (curbit == 2){
			if (cur == 1){
				return false;
			}
			else{
				num[cur] = '0';
				carryBit = 1;
			}
		}
		else{
			num[cur] = curbit + '0';
			carryBit = 0;
		}
	}
	return true;
}

void printNumber(char* num, int length){
	bool isZero = true;
	for (int i = 0; i < length; i++){
		if (num[i] != '0'){
			isZero = false;
		}
		if (!isZero){
			cout << num[i];
		}
	}
	cout << endl;
}

long long int getSystemNumber(char *num, int length, int base){
	long long int ret = 0;
	long long int weight = 1;
	int cur = length - 1;
	for (; cur >= 0; cur--){
		long long int curnum = num[cur] - '0';
		ret += (curnum*weight);
		weight *= base;
	}
	return ret;
}

bool isPrime(long long int num){
	if (num < 2){
		return false;
	}
	for (int i = 2; i <= sqrt(num); i++){
		if (num%i == 0){
			return false;
		}
	}
	return true;
}

bool isValid(char *num, int length,long long int *prims){
	for (int i = 2; i <= 10; i++){
		long long int snum = getSystemNumber(num, length, i);
		//找到是质数的因子
		bool find = false;
		for (int j = 2; j <= sqrt(snum); j++){
			if (snum%j == 0){
				prims[i] = j;
				find = true;
				break;
			}
		}
		if (!find){
			return false;
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("C-small-attempt0.in");
	streambuf* cinbuf = cin.rdbuf();
	cin.rdbuf(in.rdbuf());

	ofstream out("C-small-attempt0.out");
	streambuf* coutbuf = cout.rdbuf();
	cout.rdbuf(out.rdbuf());


	int t;
	cin >> t;
	while (t--){
		cout << "Case #" << t + 1 << ":" << endl;
		int n, j;
		cin >> n >> j;
		int off = 0;
		char* num = new char[n+1];
		memset(num, '0', n);
		num[n] = '\0';
		// 根据限制，第一位和最后一位一定是1
		num[n - 1] = num[0] = '1';
		if (n - 2 > 0){
			//保证从0开始
			num[n - 2]--;
		}
		/*while (tryNextStr(num, n)){
			cout << num << endl;
		}*/
		while (tryNextStr(num, n)){
			long long int* primes = new long long int[11];
			memset(primes, 0, sizeof(long long int) * 11);
			//printNumber(num, n);
			if (isValid(num, n, primes)){
				off++;
				cout << num;
				for (int i = 2; i <= 10; i++){
					cout << " " << primes[i];
				}
				cout << endl;
			}
			if (off == j){
				break;
			}
		}
		delete[] num;
	}
	system("pause");
	return 0;
}

