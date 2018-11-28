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
typedef long long LL;
using namespace std;
const int SIZE = 1e2+10;
const int INF = 1e9;
int dp[SIZE][SIZE][2],H[SIZE],G[SIZE];
bool fresh(int &x,int v){
    if(x<v){
        x=v;
        return true;
    }
    return false;
}
int main(){
    CASET{
        int an=0;
        DRII(P,Q);
        DRI(N);
        REP(i,N)RII(H[i],G[i]);
        MS1(dp);
        for(int i=0;;i++){
            if(Q*i>=H[0])
                break;
            int s=H[0]-Q*i;
            int need=(s+P-1)/P;
            if(need<=i+1){
                dp[0][i+1-need][0]=G[0];
            }
        }
        for(int i=0;;i++){
            if(P*i>=H[0])break;
            int s=H[0]-P*i;
            int need=(s+Q-1)/Q;
            if(i<=need){
                dp[0][need-i][1]=0;
            }
        }
        REPP(i,1,N){
            for(int j=0;j<SIZE;j++){
                for(int k=0;;k++){
                    if(Q*k>=H[i])break;
                    int s=H[i]-Q*k;
                    int need=(s+P-1)/P;
                    if(dp[i-1][j][0]!=-1){
                        if(need-j<=k){
                            fresh(dp[i][k-need+j][0],dp[i-1][j][0]+G[i]);
                        }
                    }
                    if(dp[i-1][j][1]!=-1){
                        if(need-j<=k+1){
                            fresh(dp[i][k+1-need+j][0],dp[i-1][j][1]+G[i]);
                        }
                    }
                }
                for(int k=0;;k++){
                    if(P*k>=H[i])break;
                    int s=H[i]-P*k;
                    int need=(s+Q-1)/Q;
                    if(dp[i-1][j][0]!=-1){
                        if(k-j<=need-1)fresh(dp[i][need-1-k+j][1],dp[i-1][j][0]);
                    }
                    if(dp[i-1][j][1]!=-1){
                        if(k-j<=need)fresh(dp[i][need-k+j][1],dp[i-1][j][1]);
                    }
                }
            }
        }
        /*
        REP(i,N){
            REP(j,5)printf("(%d,%d)",dp[i][j][0],dp[i][j][1]);
            puts("");
        }*/
        REP(i,SIZE){
            an=max(an,dp[N-1][i][0]);
            an=max(an,dp[N-1][i][1]);
        }
        printf("Case #%d: %d\n",case_n++,an);
    }
    return 0;
}
