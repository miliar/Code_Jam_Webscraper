// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

/*
int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}
*/


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
typedef long long ll;


int check(char *line, int n) {
	int k;
	for (k = 0; k < n; ++k) {
		if (line[k] == '-') {
			break;
		}
	}
	if (k == n) {
		return 1;
	}
	else {
		return 0;
	}
}

int main(void) {
	FILE *fp = fopen("test.txt", "rt");
	if (fp == NULL) {
		printf("failed to open file\n");
		return -1;
	}

	#define MAX_LINE_SIZE 0x1000
	char line[MAX_LINE_SIZE];

	int case_num;
	fgets(line, MAX_LINE_SIZE, fp);
	case_num = strtol(line, NULL, 10);
	
	for (int i = 1; i <= case_num; ++i) {
		printf("Case #%d: ", i);

		// - +
		fgets(line, MAX_LINE_SIZE, fp);
		int n = strlen(line) - 1;	// -1 = crlf
		

		// check
		if (check(line, n)) {
			printf("0");
		}
		else {

			// flip
			int count = 0;
			int index = n - 1;
			if (line[index] == '-') {
				++count;
				char c = '-';
				while (--index >= 0) {
					if (line[index] != c) {
						++count;
						c = line[index];
					}
				}
				printf("%d", count);

			}
			else {
				char c = '+';
				while (--index >= 0) {
					if (line[index] != c) {
						++count;
						c = line[index];
					}
				}
				printf("%d", count);
			}
			
		}




		puts("");

	}

	fclose(fp);
}