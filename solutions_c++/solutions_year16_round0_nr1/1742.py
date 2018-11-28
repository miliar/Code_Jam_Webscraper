// ConsoleApplication6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cstring>
#include <queue>
#include <algorithm>
#include <climits>
#include <string>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <cstdio>
#include <list>
#include <set>
#include <iterator>



using namespace std;



long long N;
bool Digits[10] = { false, };

bool isAlltrue(bool* array) {

	return (Digits[0] && Digits[1] && Digits[2] && Digits[3] && Digits[4] && Digits[5] &&
		Digits[6] && Digits[7] && Digits[8] && Digits[9] && Digits);


}

void num2digit(long long number) {

	long long tmp;

	while (number)
	{
		tmp = number % 10;
		number /= 10;
		Digits[tmp] = true;
	}
}


int main() {

	int cnt = 1;
	int count = 1;

	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("res.out");

	int T;
	fin >> T;
	

	for (int i = 0; i < T; i++) {
		
		fin >> N;

		while (true) {

			if (N == 0) {
				fout << "Case #" << count << ": " << "INSOMNIA" << endl;
				count++;
				break;
			}

			num2digit(cnt*N);
			if (isAlltrue(Digits)) {
				fout << "Case #" << count << ": " << cnt*N << endl;
				count++;
				break;
			}

			cnt++;

		}
		cnt = 1;
		memset(Digits, false, sizeof(Digits));


	}

	fin.close();
	fout.close();

	system("pause");

	return 0;
}



