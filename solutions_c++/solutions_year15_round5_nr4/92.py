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
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define F first
#define S second
typedef long long LL;
using namespace std;
const int MOD = 1e9+7;
const int SIZE = 1e6+10;
// template end here
map<int,int>H;
PII pp[SIZE];
int main(){
    CASET{
        H.clear();
        int num=0;
        DRI(P);
        REP(i,P)RI(pp[i].F);
        REP(i,P)RI(pp[i].S);
        REP(i,P){
            H[pp[i].F]+=pp[i].S;
            num+=pp[i].S;
        }
        printf("Case #%d:",case_n++);
        for(int i=0;(1<<i)<num;i++){
            map<int,int>::iterator it=H.begin();
            int me;
            if(it->S==1){
                it++;
                me=it->F;
            }
            else me=0;
            printf(" %d",me);
            map<int,int>H2,H3;
            if(me==0){
                for(it=H.begin();it!=H.end();it++){
                    H3[it->F]=it->S/2;
                }
            }
            else{
                for(it=H.begin();it!=H.end();it++){
                    int now=it->S-H2[it->F];
                    if(!now)continue;
                    H3[it->F]=now;
                    H2[it->F+me]=now;
                }
            }
            H=H3;
        }
        puts("");
    }
    return 0;
}
