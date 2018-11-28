
// Google Template

#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <deque>
#include <queue>
#include <list>
#include <map>
#include <tuple>
#include <string.h>

FILE *f;
char* of = "C:/Users/hjp/Desktop/codejam.txt";

void init() {
	f = fopen(of, "w");
}
void done() {
	fclose(f);
}

int main(int argc, char *argv[])
{
	init();

	char buf[1000 + 10];
	char clearend[16];
	int shyness[1000 + 10];
	int cases;
	scanf("%d", &cases);	gets(clearend);
	for (int c = 0; c < cases; c++) {
		int maxshyness = 0;
		scanf("%d%s", &maxshyness, buf);	gets(clearend);
		for (int i = 0; i <= maxshyness; ++i) {
			shyness[i] = buf[i] - '0';
		}
		int acc = 0, need = 0;
		for (int i = 0; i <= maxshyness; ++i) {
			if (acc >= i) {
				acc += shyness[i];
			} else {
				need += i - acc;
				acc = i + shyness[i];
			}
		}
		fprintf(f, "Case #%d: %d\n", c + 1, need);
	}
		
	done();
}

