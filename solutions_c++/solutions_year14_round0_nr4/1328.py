#include <iostream>
#include <string.h>  
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <algorithm>

using namespace std;

int cmp(const void *x, const void *y)
{
  double xx = *(double*)x, yy = *(double*)y;
  if (xx < yy) return -1;
  if (xx > yy) return  1;
  return 0;
}

#define MAXN 1024
int N;
double A[MAXN], B[MAXN];
bool U[MAXN], V[MAXN];

int war() {
    int sN = 0;
    memset(U, 0, MAXN);
    memset(V, 0, MAXN);
    for (int i = 0; i < N; i++) {
        double cN = A[i];
        int mK = -1, cK = -1;
        for (int j = 0; j < N; j++)
            if (!V[j] && (mK < 0 || B[j] < B[mK]))
                mK = j;
        for (int j = 0; j < N; j++)
            if (!V[j] && B[j] > cN && (cK < 0 || B[j] < B[cK]))
                cK = j;
        int sK = cK >= 0? cK : mK;
        if (cK >= 0) V[cK] = 1;
        else V[mK] = 1, sN++;
    }
    return sN;
}

bool bpGraph[MAXN][MAXN];
bool seen[MAXN];
int matchR[MAXN];

bool bpm(int u) {
    for (int v = 0; v < N; v++) {
        if (bpGraph[u][v] && !seen[v]) {
            seen[v] = true;
            if (matchR[v] < 0 || bpm(matchR[v])) {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}
 
int maxBPM() {
    memset(matchR, -1, sizeof(matchR));
    int result = 0;
    for (int u = 0; u < N; u++) {
        memset(seen, 0, sizeof(seen));
        if (bpm(u))
            result++;
    }
    return result;
}

int dwar() {
    int sN = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            bpGraph[i][j] = A[i] > B[j];
    return maxBPM();
}

int main() {
    ifstream fin("D2.in");
    fstream fout("D.out", ios::out);
    int T;
    fin >> T;
    for (int zzz = 1; zzz <= T; zzz++) {
        fin >> N;
        for (int i = 0; i < N; i++) fin >> A[i];
        for (int i = 0; i < N; i++) fin >> B[i];
        qsort(A, N, sizeof(double), cmp);
        qsort(B, N, sizeof(double), cmp);
        fout << "Case #" << zzz << ": " << dwar() << " " << war() << endl;
    }
    fout.close();
    return 0;
}
