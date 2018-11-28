/* 
 * File:   main.cpp
 * Author: Yiting
 *
 * Created on April 13, 2013, 8:52 AM
 */

#include <cstdlib>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<cmath>
#define DEBUG 1
using namespace std;

int T, r, t, res;
long current;

#if DEBUG
FILE *fin = fopen("test.in", "rb");
FILE *fout = fopen("test.out", "wb");
#else
FILE *fin = fopen("inflate.in", "rb");
FILE *fout = fopen("inflate.out", "wb");
#endif

void solve(int circle) {
    if (circle == 1) {
        current = current + (r + 1)*(r + 1) - r*r;
    } else {
        current = current + (r + 2 * circle - 1)*(r + 2 * circle - 1) - (r + 2 * circle - 2)*(r + 2 * circle - 2);
    }
}

int main() {
    fscanf(fin, "%d", &T);
    int i;
    for (i = 0; i < T; i++) {
        fscanf(fin, "%d %d", &r, &t);
        res = 1, current = 0;
        while (1) {
            solve(res);
            if (current > t) {
                res--;
                break;
            }
            res++;
        }
        fprintf(fout, "Case #%d: %d\n", i + 1, res);
    }
    return 0;
}

