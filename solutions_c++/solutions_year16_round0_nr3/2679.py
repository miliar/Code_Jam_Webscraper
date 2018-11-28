//
//  main.cpp
//  codejam_3
//
//  Created by 김 균태 on 2016. 4. 9..
//  Copyright © 2016년 ethan. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <vector>
#include <deque>
#include <queue>
#include <unordered_map>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <math.h>

using namespace std;

const int N = 16;
const int until = 50;
int A[N];
unsigned long long num[11], arr_divisor[11];
int c = 0;

void incA() {
	int i = 1;
	for (;;) {
		if (A[i] == 1) {
			A[i] = 0;
			++i;
		} else {
			A[i] = 1;
			break;
		}
	}
	for (unsigned long long i = 2; i <= 10; ++i) {
		unsigned long long base = i;
		unsigned long long result = 1;
		for (int j = 1; j < N; ++j) {
			if (A[j] == 1) {
				result += base;
			}
			base *= i;
		}
		num[i] = result;
	}
}

unsigned long long getDivisor(unsigned long long num) {
	if (num % (unsigned long long)2 == 0) {
		return (unsigned long long)2;
	}
	
	unsigned long long til = (unsigned long long)sqrt((double)num);
	for (unsigned long long i = 3; i <= til; i += 2) {
		if (num % i == 0) {
			return i;
		}
	}
	
	return num;
}

int main(int argc, const char * argv[]) {
	for (int i = 0; i < N; ++i) {
		A[i] = 0;
	}
	A[0] = A[N-1] = 1;
	for (unsigned long long i = 2; i <= 10; ++i) {
		unsigned long long base = 1;
		for (unsigned long long j = 1; j < N; ++j) {
			base *= i;
		}
		num[i] = (unsigned long long)1 + base;
	}
	
	ofstream writeFile;
	writeFile.open("output1.txt");
	
	printf("Case #1:\n");
	writeFile << "Case #1:\n";
	
	do {
		bool allfind = true;
		for (unsigned long long i = 2; i <= 10; ++i) {
			if (allfind) {
				unsigned long long acc = num[i];
				unsigned long long divisor = getDivisor(acc);
				if (divisor == acc) {
					allfind = false;
					break;
				} else {
					arr_divisor[i] = divisor;
				}
			}
		}
		if (allfind) {
			for (int i = N-1; i >= 0; --i) {
				printf("%d", A[i]);
				writeFile << A[i] << "";
			}
			printf(" ");
			writeFile << " ";
			
			for (int i = 2; i <= 10; ++i) {
				printf("%llu ", arr_divisor[i]);
				writeFile << arr_divisor[i] << " ";
			}
			printf("\n");
			writeFile << "\n";
			c++;
			printf("%d\n", c);
		}
		incA();
	} while (c < until);
	
	writeFile.close();
	return 0;
}
