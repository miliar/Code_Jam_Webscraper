/*
 *  Problem2.cpp
 *  
 *
 *  Created by sean brown on 14-05-03.
 *  Copyright 2014 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>

using namespace std;

int main() {

	int tests, a, b, k;
	int total = 0;
	int lookup[1000][1000];
	FILE* input;
	FILE* output;
	
	const char* inFile = "B-small-attempt0.in";
	const char* outFile = "B-small-attempt0.out";
	
	input = fopen(inFile, "r");
	output = fopen(outFile, "w");
	
	for (int i = 0; i < 1000; i++) {
		for (int j = 0; j < 1000; j++) {
			lookup[i][j] = i & j;
		}
	}
	fscanf(input, "%d", &tests);
	for (int i = 0; i < tests; i++) {
		fscanf(input, "%d %d %d", &a, &b, &k);
		
		for (int j = 0; j < a; j++) {
			for (int h = 0; h < b; h++) {
				if (lookup[j][h] < k) {
					total++;
				}
			}
		}
		
		fprintf(output, "Case #%d: %d\n", i+1, total);
		total = 0;
	}
	
	fclose(input);
	fclose(output);
}