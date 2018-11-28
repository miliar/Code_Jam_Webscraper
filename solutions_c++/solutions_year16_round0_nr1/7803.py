#pragma once
#include <fstream>
#include <iostream>
#include <conio.h>
#include <set>
using namespace std;

int main() {
	ifstream fin("sheep_small.in");
	ofstream fout("sheep_small.out");
	long long N, result, remainder;
	int T, unit;
	set<int> digits;
	fin >> T;
	for (int i = 0; i < T; i++) {
		result = 0;
		digits.clear();
		fin >> N;
		for (int j = 1; ; j++) {
			remainder = N * j;
			do {
				unit = remainder % 10;
				remainder /= 10;
				digits.insert(unit);
			} while (remainder != 0 && digits.size() < 10);
			if (digits.size() == 10 || N==0) {
				result = N*j;
				break;
			}
		}
		if(result==0)
			fout << "Case #" << i + 1 << ": INSOMNIA"<<endl;
		else
			fout << "Case #" << i + 1 << ": " << result<<endl;
	}
}