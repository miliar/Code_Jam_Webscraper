// practice.cpp : Defines the entry point for the console application.
#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
#define ll long long int

int crosschk(int arr[]) {
	for (int j = 0;j<10;j++) {
		if (arr[j] == 0) return 0;
	}
	return 1;
}

void check(ll val, int ar[]) {

	while (val != 0) {
		int num = val % 10;
		ar[num]++;
		val /= 10;
	}
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int t;
	fin >> t;
	for (int ai = 1;ai <= t;ai++) {
		ll n, res = 0;
		fin >> n;
		if (n == 0) fout << "Case #" << ai << ": " << "INSOMNIA" << endl;
		else {
			int i = 1;
			int a[10] = { 0,0,0,0,0,0,0,0,0,0 };
			while (crosschk(a) != 1) {
				res = i*n;
				ll temp = res;
				check(temp, a);
				i++;
				res = 0;
			}
			fout << "Case #" << ai << ": " << (i - 1)*n << endl;
		}
	}
	// your code goes here
	return 0;
}




