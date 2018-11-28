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

		// n
		fgets(line, MAX_LINE_SIZE, fp);
		int n = strtol(line, NULL, 10);
		// printf("%d", n);
		if (n == 0) {
			printf("INSOMNIA"); 
		}
		else {
			int nSlept = 0;
			int slept[10] = {0};
			int finish = 0;
			for (int j = 1; j < 1000; ++j) {
				long long nn = n * j;
				long long nnn = nn;
				for (int i = 0; i < 10; ++i) {
					int k = (nn % 10); nn /= 10;
					if (slept[k] == 0) {
						slept[k] = 1;
						++nSlept;
						if (nSlept == 10) {
							printf("%d", nnn);
							finish = 1;
							break;
						}
					}
					if (nn == 0) {
						break;
					}
				}
				if (finish) {
					break;
				}
			}

			if (!finish) {
				printf("INSOMNIA"); 
			}
		}

		puts("");

	}

	fclose(fp);
}