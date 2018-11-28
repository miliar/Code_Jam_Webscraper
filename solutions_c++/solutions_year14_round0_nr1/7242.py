#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <stack>
#include <cstring>
#include <vector>
#include <string>
#include <cctype>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>
#define inf 0x7fffffff
#define MOD 1000000007

using namespace std;

int main() {
	FILE* in = fopen("A-small-attempt1 (1).in", "r");
	FILE* out = fopen("A-small-attempt1 (1).out", "w");
	int t;
	fscanf(in, "%d", &t);
	bool f[17];

	for(int ca=1; ca<=t; ca++) {
		int i, j;
		for(i=0; i<17; i++)
			f[i] = false;
		int row;
		fscanf(in, "%d", &row);
		int num;
		for(i=1; i<5; i++) {
			for(j=1; j<5; j++) {
				fscanf(in, "%d", &num);
				if(i == row)
					f[num] = true;
			}
		}
		int res = 0, cnt = 0;
		fscanf(in, "%d", &row);
		for(i=1; i<5; i++) {
			for(j=1; j<5; j++) {
				fscanf(in, "%d", &num);
				if(i == row && f[num]) {
					cnt++;
					res = num;
				}
			}
		}
		fprintf(out, "Case #%d: ", ca);
		if(cnt == 0) {
			fprintf(out, "Volunteer cheated!\n");
		} else {
			if(cnt == 1) {
				fprintf(out, "%d\n", res);
			} else {
				fprintf(out, "Bad magician!\n");
			}
		}
	}
	fclose(in);
	fclose(out);

	return 0;
}