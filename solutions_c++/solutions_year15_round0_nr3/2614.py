#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

inline int floor(int a) {
	return a / 2 + a % 2;
}

int Matrix[4][4] = {
	{'1', 'i', 'j', 'k'},
	{'i', -'1', 'k', -'j'},
	{'j', -'k', -'1', 'i'},
	{'k', 'j', -'i', -'1'}
};

int InverseMatrix[4][4] = {
	{'1', 'i', 'j', 'k'},
	{'i', '1', -'k', 'j'},
	{'j', 'k', '1', -'i'},
	{'k', -'j', 'i', '1'}
};

int convert(char ch) {
	switch (ch) {
		case '1': case -'1': return 0;
		case 'i': case -'i': return 1;
		case 'j': case -'j': return 2;
		case 'k': case -'k': return 3;
	}
	return -1;
}

int main()
{
	int testcases;
	FILE *pFile = fopen("C-small-attempt0.in", "r");
	FILE *outFile = fopen("c-small.out", "w");
	fscanf(pFile, "%d", &testcases);
	for (int tc=1; tc<=testcases; tc++) {
		int values[10010]; memset(values, 0, sizeof values);
		fprintf(outFile, "Case #%d: ", tc);
		int L, X;
		char str[10010];
		fscanf(pFile, "%d%d", &L, &X);
		fscanf(pFile, "%s", str);
		for (int j=0; j<X; ++j) {
			for (int i=0; i<L; ++i) {
				int index = i + j * L;
				if (index == 0) {
					values[index] = str[i];
				} else {
					int previous = values[index-1];
					int negative = previous < 0 ? -1 : 1;
					values[index] = negative * Matrix[convert(previous)][convert(str[i])];
				}
			}
		}
		if (values[X * L - 1] != -'1') {
			fprintf(outFile, "NO\n");
		} else {
			bool found = false;
			for (int i=0, size=L*X; i<size; ++i) {
				if (values[i] == 'i') {
					for (int j=i+1; j<size; ++j) {
						if (InverseMatrix[convert(values[i])][convert(values[j])] == 'j') {
							if (InverseMatrix[convert(values[j])][convert(values[X * L - 1])] == 'k') {
								found = true;
								goto found;
							}
						}
					}
				}
			}
found:
			if (found) {
				fprintf(outFile, "YES\n");
			} else {
				fprintf(outFile, "NO\n");
			}
		}
	}

	return 0;
}