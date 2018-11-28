#include<stdio.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<bitset>
#include<map>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define REPC(I, C) for (int I = 0; !(C); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
#define ULL unsigned long long
#define MAXN 5   
using namespace std;

int mat1[MAXN][MAXN];
int mat2[MAXN][MAXN];

int main()
{
    CASET {
        DRI(r1);
        REP(i, 4) REP(j, 4)
            RI(mat1[i][j]);
        DRI(r2);
        REP(i, 4) REP(j, 4)
            RI(mat2[i][j]);
        int ans = -1;
        int cnt = 0;
        REP(i, 4) REP(j, 4)
            if(mat1[r1-1][i]==mat2[r2-1][j])
            {
                ans = mat1[r1-1][i];
                cnt++;
            }
        printf("Case #%d: ", case_n);        
        if(cnt == 0)
            printf("Volunteer cheated!\n");
        else if(cnt > 1)
            printf("Bad magician!\n");
        else
            printf("%d\n", ans);
        ++case_n;
    }
    return 0;
}
