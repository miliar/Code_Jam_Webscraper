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

int find_winner(vector<double> &in, int st, int ed, double val)
{
    int idx = 0;
    int md = 0;
    while(st <= ed) {
        md = (st + ed)/2;
        if(in[md]==val) break;
        else if(in[md] > val) ed = md - 1;
        else st = md + 1;            
    }
    if(in[md] > val) return md;
    if(in[md]==val) return md + 1;
    else
        return md + 1;
}

int main()
{
    CASET {
        DRI(sz);
        vector<double> her(sz, 0);
        vector<double> his(sz, 0);
        REP(i, sz)
            scanf("%lf", &her[i]);
        REP(i, sz)
            scanf("%lf", &his[i]);
        sort(ALL(his));
        sort(ALL(her));
        /*
        REP(i, sz)
            printf("%lf ", her[i]);
        printf("\n");
        REP(i, sz)
            printf("%lf ", his[i]);
        printf("\n");
        int sc1 = 0, sc2 = 0;
        int st = 0, ed = sz - 1;
        for(int i=sz-1;i>=0;i--)
        {
            if(her[i]>his[ed]) continue;
            ed = find_winner(his, st, ed, her[i]);
            if(his[ed] < her[i]) break;
            ed--;
            ++sc2;
        }
        
        st = 0, ed = sz - 1;
        for(int i=sz-1;i>=0;i--)
        {
            if(his[i]>her[ed]) continue;           
            ed = find_winner(her, st, ed, his[i]);
            printf("index = %d\n", ed);
            ed--;
            ++sc1;
        }
        */
        int sc1 = 0;
        int i=sz-1,j=sz-1;
        while(true) {
            if(her[i] > his[j]) {
                --i;
                --j;
                ++sc1;
            }else{
                --j;
            }
            if(i<0 || j<0) break;
        }
        
        int sc2 = 0;
        i=sz-1, j=sz-1;
        while(true) {
            if(his[i] > her[j]) {
                --i;
                --j;
                ++sc2;
            }else{
                --j;
            }
            if(i<0 || j<0) break;
        }
        printf("Case #%d: %d %d\n", case_n, sc1, sz - sc2);
        case_n++;
    }
    return 0;
}
