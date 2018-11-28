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
const int SIZE = 1e6+6;
LL a[SIZE];
LL get(int L,int R){
    if(L>R)return 0;
    if(!L)return a[R];
    return a[R]-a[L-1];
}
int main(){
    CASET{
        LL p,q,r,s;
        DRI(N);
        cin>>p>>q>>r>>s;
        REP(i,N){
            a[i+1]=(i*p+q)%r+s;
        }
        REPP(i,1,N+1)a[i]+=a[i-1];
        LL mi=1e18;
        for(int i=N;i>0;i--){
            LL now=get(i,N);
            int ll=1,rr=N;
            while(ll<rr){
                int mm=(ll+rr+1)>>1;
                if(get(1,mm-1)>get(mm,i))rr=mm-1;
                else ll=mm;
            }
            int mm=ll;
            LL ma=max(max(get(1,mm-1),get(mm,i)),get(i+1,N));
            mi=min(mi,ma);
            if(mm<i){
                mm++;
                ma=max(max(get(1,mm-1),get(mm,i)),get(i+1,N));
                mi=min(mi,ma);
            }
        }
        printf("Case #%d: %.12f\n",case_n++,1.-mi*1./get(1,N));
    }
    return 0;
}
