#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
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
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define VPLL vector<pair<long long,long long> >
#define F first
#define S second
typedef long long LL;
using namespace std;
const int MOD = 1e9+7;
const int SIZE = 1e6+10;
int d[3],d2[3];
char c[8]="RPS";
int lv[13][4096];
void repermutation(int ker[],int n){
    if(n==1)return;
    repermutation(ker,n/2);
    repermutation(ker+n/2,n/2);
    bool big=0;
    REP(i,n/2){
        if(c[ker[i]]!=c[ker[i+n/2]]){
            if(c[ker[i]]>c[ker[i+n/2]]){
                big=1;
            }
            break;
        }
    }
    if(big){
        REP(i,n/2)swap(ker[i],ker[i+n/2]);
    }
}
int main(){
    CASET{
        DRI(N);
        N=1<<N;
        REP(i,3)RI(d[i]);
        int two=1;
        bool err=0;
        while(two<N&&!err){
            if((d[0]+d[2]-d[1])%2){
                err=1;
                break;
            }
            d2[0]=(d[0]+d[2]-d[1])/2;
            d2[1]=(d[0]+d[1]-d[2])/2;
            d2[2]=(d[1]+d[2]-d[0])/2;
            REP(i,3){
                d[i]=d2[i];
                if(d[i]<0)err=1;
            }
            two*=2;
        }
        printf("Case #%d: ",case_n++);
        if(err)puts("IMPOSSIBLE");
        else{
            int it=0;
            REP(i,3){
                if(d[i])lv[it][0]=i;
            }
            int now=1;
            while(now<N){
                REP(i,1<<it){
                    lv[it+1][i*2]=lv[it][i];
                    lv[it+1][i*2+1]=(lv[it][i]+2)%3;
                }
                now*=2;
                it++;
            }
            repermutation(lv[it],1<<it);
            REP(i,1<<it)printf("%c",c[lv[it][i]]);
            puts("");
        }
    }
    return 0;
}
