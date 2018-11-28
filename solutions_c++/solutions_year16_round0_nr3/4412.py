
#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;


long long prime(long long n)
{
	long long t = (int)(sqrt(n) + 1);
	for (long long i = 3; i <= t; i++) {
		if (n % i == 0) return i;
	}
	return n;
}

bool jamcoin(int arr[], long long divisors[], int n)
{
	for (int i = 2; i <= 10; i++) {
		long long num = 0;
		for (int j = 0; j < n; j++) {
			num = num * i + arr[j];
		}
		divisors[i - 1] = prime(num);
		if (divisors[i - 1] == num) return false;
	}
	return true;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int cases, n, count;
	long long divisors[10];
	int arr[100];

	fin >> cases;
	for (int t = 1; t <= cases; t++) {

		fin >> n >> count;
		fout << "Case #" << t << ": " << endl;

		int max_num = 1 << n;

		int cur_cnt = 0;
		for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2) {
			
			int tmp = i;
			for (int j = n - 1; j >= 0; j--) {
				arr[j] = tmp % 2;
				tmp = tmp / 2;
			}
			if (jamcoin(arr, divisors, n)) {
				for (int j = 0; j < n; j++) {
					fout << arr[j];
				}
				for (int j = 1; j < 10; j++) {
					fout << " " << divisors[j];
				}
				fout << endl;
				cur_cnt++;
				if (cur_cnt == count) break;
			}
		}	
	}

	fin.close();
	fout.close();
	return 0;
}
