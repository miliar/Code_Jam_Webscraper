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
#define F first
#define S second
typedef long long LL;
using namespace std;
int a[11111];
multiset<int>H;
int main(){
    CASET{
        DRII(N,X);
        H.clear();
        REP(i,N){
            RI(a[i]);
            H.insert(a[i]);
        }
        int an=0;
        while(SZ(H)){
            int ma=*H.rbegin();
            if(ma+ma<=X){
                an+=(SZ(H)+1)/2;
                break;
            }
            an++;
            H.erase(H.find(ma));
            multiset<int>::iterator it=H.upper_bound(X-ma);
            if(it!=H.begin()){
                it--;
                H.erase(it);
            }
        }
        printf("Case #%d: %d\n",case_n++,an);
    }
    return 0;
}
