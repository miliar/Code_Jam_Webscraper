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
FILE *fin  = fopen("a.in",  "r");
FILE *fout = fopen("gcj-a.out", "w");

int main () {
	int T;
    int r1, r2, r1a[4], r2a[4], x;

	fscanf(fin, "%d", &T);

    for(int t = 1; t <= T; t++) {
        fscanf(fin, "%d", &r1); r1--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                fscanf(fin, "%d", &x);
                if(i == r1) r1a[j] = x;
            }
        }
        fscanf(fin, "%d", &r2); r2--;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                fscanf(fin, "%d", &x);
                if(i == r2) r2a[j] = x;
            }
        }

        //cout << r1a[0] << " " << r1a[1] << " " << r1a[2] << " " << r1a[3] << endl;
        //cout << r2a[0] << " " << r2a[1] << " " << r2a[2] << " " << r2a[3] << endl;

        // Check if unique
        int col = -1;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(r1a[i] == r2a[j]) {
                    if(col == -1) col = r1a[i];
                    else {col = -2;}
                }
            }
        }

        if(col == -2) {
            fprintf(fout, "Case #%d: Bad magician!\n", t);
        } else if (col == -1) {
            fprintf(fout, "Case #%d: Volunteer cheated!\n", t);
        } else {
            fprintf(fout, "Case #%d: %d\n", t, col);
        }
    }

	return 0;
}


