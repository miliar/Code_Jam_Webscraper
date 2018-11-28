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
	int T,N,M, field[105][105];
	fscanf(fin, "%d", &T);

    for(int t = 1; t <= T; t++) {
        fscanf(fin, "%d %d", &N, &M);
        for(int r = 0; r < N; r++) {
            for(int c = 0; c < M; c++) {
                fscanf(fin, "%d", &field[r][c]);
            }
        }
        bool bad = false;
        for(int a = 1; a <= 100; a++) {
            for(int r = 0; r < N; r++) {
                int actr = 0;
                for(int c = 0; c < M; c++)
                    if(field[r][c] == a || field[r][c] == 1000) actr++;
                if(actr == M) {
                    for(int c = 0; c < M; c++)
                        field[r][c] = 1000;
                }
            }
            for(int c = 0; c < M; c++) {
                int actr = 0;
                for(int r = 0; r < N; r++)
                    if(field[r][c] == a || field[r][c] == 1000) actr++;
                if(actr == N) {
                    for(int r = 0; r < N; r++)
                        field[r][c] = 1000;
                }
            }
            for(int r = 0; r < N; r++) 
                for(int c = 0; c < M; c++) 
                    if(field[r][c] == a) 
                        bad = true;
            if(bad) break;                    
        }
        if(bad)
            fprintf(fout, "%s%d%s\n", "Case #", t, ": NO");
        else
            fprintf(fout, "%s%d%s\n", "Case #", t, ": YES");
    }

	return 0;
}


