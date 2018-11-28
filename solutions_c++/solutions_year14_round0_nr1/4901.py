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
using namespace std;
int d[4][4],cnt[17];
int main(){
    CASET{
        DRI(r1);
        MS0(cnt);
        REP(i,4)REP(j,4)RI(d[i][j]);
        REP(i,4)cnt[d[r1-1][i]]++;
        RI(r1);
        REP(i,4)REP(j,4)RI(d[i][j]);
        REP(i,4)cnt[d[r1-1][i]]++;
        vector<int>an;
        REP(i,17){
            if(cnt[i]==2)an.PB(i);
        }
        printf("Case #%d: ",case_n++);
        if(SZ(an)==0)puts("Volunteer cheated!");
        else if(SZ(an)>1)puts("Bad magician!");
        else printf("%d\n",an[0]);
    }
    return 0;
}
