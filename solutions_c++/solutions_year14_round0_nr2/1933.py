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
using namespace std;

double solutionN(double C, double F, double X, int fnum)
{
    double ans = 0.0;
    double speed = 2.0;
    
    while(fnum-- > 0) {        
        ans += C/speed;
        speed+=F;
    }
    ans += (X/speed);
    return ans;
}

int main()
{
    CASET {
        double C,F,X;
        scanf("%lf%lf%lf", &C, &F, &X);
        int range = X/F;
        double min = 10000000000000000000000.0;
        int i=0;
        while(true) {
            double tmp = solutionN(C, F, X, i);
            if(tmp <= min)
                min = tmp;
            else break;
            ++i;
        }
        printf("Case #%d: %.7lf\n", case_n, min);
        ++case_n;
    }
    return 0;
}
