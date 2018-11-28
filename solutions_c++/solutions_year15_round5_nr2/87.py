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
const int SIZE = 1e3+10;
// template end here
int sum[SIZE];
int ma[SIZE],mi[SIZE];
int main(){
    CASET{
        DRII(N,K);
        REP(i,N-K+1)RI(sum[i]);
        for(int i=0;i<K;i++){
            ma[i]=mi[i]=0;
            int now=0;
            for(int j=i;j+K<N;j+=K){
                now+=sum[j+1]-sum[j];
                ma[i]=max(ma[i],now);
                mi[i]=min(mi[i],now);
            }
        }
        int V=-1,id;
        REP(i,K){
            if(ma[i]-mi[i]>V){
                V=ma[i]-mi[i];
                id=i;
            }
        }
        LL ll=0,rr=0;
        REP(i,K){
            ll+=mi[id]-mi[i];
            rr+=ma[id]-ma[i];
        }
        printf("Case #%d: ",case_n++);
        if(rr-ll>=K)printf("%d\n",V);
        else{
            bool suc=0;
            for(LL i=ll;i<=rr;i++){
                if((sum[0]-i)%K==0)suc=1;
            }
            if(suc)printf("%d\n",V);
            else printf("%d\n",V+1);
        }
        
    }
    return 0;
}
