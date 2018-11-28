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
FILE *fin  = fopen("d.in",  "r");
FILE *fout = fopen("gcj-d.out", "w");

int main () {
	int T, N, a1, a2;
	double x;

    fscanf(fin, "%d", &T);
    for(int t = 1; t <= T; t++) {
        vector<pair<double, char> > vals;
        a1 = 0; a2 = 0;
        fscanf(fin, "%d", &N);
        for(int i = 0; i < N; i++) {
            fscanf(fin, "%lf", &x);
            vals.push_back(make_pair(x, 'n'));
        }
        for(int i = 0; i < N; i++) {
            fscanf(fin, "%lf", &x);
            vals.push_back(make_pair(x, 'k'));
        }
        sort(vals.begin(), vals.end());

        int ctr = 0;
        for(int i = 0; i < vals.size(); i++) {
            if(vals[i].second == 'n') ctr++;
            else {
                if(ctr > 0) ctr--;
                else a1++;
            }
        }
        ctr = 0;
        for(int i = 0; i < vals.size(); i++) {
            if(vals[i].second == 'k') ctr++;
            else {
                if(ctr > 0) ctr--;
                else a2++;
            }
        }
        a2 = N - a2;

        fprintf(fout, "Case #%d: %d %d\n", t, a2, a1);
        //printf("Case #%d: %d %d\n", t, a2, a1);
    }

	return 0;
}


