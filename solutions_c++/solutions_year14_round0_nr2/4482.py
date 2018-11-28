/*
LANG: C++
ID: 2012agura1
*/

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

int main () {
	int T;
	double c, f, x;
	double sold, snew, ssum;

    fscanf(fin, "%d", &T);
    for(int t = 1; t <= T; t++) {
        fscanf(fin, "%lf %lf %lf", &c, &f, &x);
        //cout << c << " " << f << " " << x << endl;
        sold = 1e20;
        snew = x/2.0;
        ssum = 0;
        for(int k = 0; snew <= sold; k++) {
            sold = snew;
            ssum += c / (2 + k * f);
            snew = ssum + x / (2 + (k+1) * f);
            //cout << k << ": " << sold << " => " << snew << endl;
        }

        fprintf(fout, "Case #%d: %f\n", t, sold);
        //printf("Case #%d: %f\n", t, sold);
    }

	return 0;
}


