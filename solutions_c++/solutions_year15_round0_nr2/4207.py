#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <ctime>

using namespace std;
FILE *fin  = fopen("b.in",  "r");
FILE *fout = fopen("gcj-b.out", "w");

int a[1000];
int main () {
    int T, D;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++) {
		fscanf(fin, "%d", &D);
		for(int i = 0; i < D; i++) fscanf(fin, "%d", &a[i]);
		int res = 10000;
		for(int k = 1; k <= 1000; k++) {
			int r = 0;
			for(int i = 0; i < D; i++) {
				if(a[i] > k) {
					r += (a[i] - k)/k + (a[i] % k != 0);
				}
			}
			res = min(res, k+r);
		}
		fprintf(fout, "Case #%d: %d\n", t, res);
	}
	return 0;
}
