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
int an;
int d[SIZE];
vector<int>e[SIZE];
int S[SIZE],M[SIZE];
int N,D;
int cnt;
void dfs(int x,int st){
    if(S[x]>st+D||S[x]<st)return;
    cnt++;
    REP(i,SZ(e[x])){
        dfs(e[x][i],st);
    }
}
int main(){
    CASET{
        an=0;
        MS0(d);
        RII(N,D);
        int S0,As,Cs,Rs,M0,Am,Cm,Rm;
        cin>>S0>>As>>Cs>>Rs;
        cin>>M0>>Am>>Cm>>Rm;
        S[0]=S0;
        M[0]=M0;
        REP(i,N)e[i].clear();
        REPP(i,1,N){
            S[i]=((LL)S[i-1]*As+Cs)%Rs;
            M[i]=((LL)M[i-1]*Am+Cm)%Rm;
            e[M[i]%i].PB(i);
        }
        REPP(i,S[0]-D,S[0]+1){
            cnt=0;
            dfs(0,i);
            an=max(an,cnt);
        }
        printf("Case #%d: %d\n",case_n++,an);
    }
    return 0;
}
