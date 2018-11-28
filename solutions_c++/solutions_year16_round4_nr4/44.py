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
const int INF = 1e9+7;
const int SIZE = 1000;
char s[30][30];
int n;
int sqr(int x){return x*x;}
struct Union_Find{
    int d[SIZE],num[SIZE];
    void init(int n){
        REP(i,n)d[i]=i,num[i]=1;
    }
    int find(int x){
        return (x!=d[x])?(d[x]=find(d[x])):x;
    }
    bool uu(int x,int y){
        x=find(x);
        y=find(y);
        if(x==y)return 0;
        if(num[x]<=num[y]){
            num[y]+=num[x];
            d[x]=y;
        }
        else{
            num[x]+=num[y];
            d[y]=x;
        }
        return 1;
    }
}U;
PII dd[25];
int dn;
int dp[1<<17][26];
PII sum[1<<25];
template <class T>
void maa(T& x,T y){
    if(x<y)x=y;
}
template <class T>
void mii(T& x,T y){
    if(x==-1||x>y)x=y;
}
int main(){
    CASET{
        int oo=0;
        RI(n);
        U.init(2*n);
        REP(i,n)RS(s[i]);
        REP(i,n)REP(j,n){
            if(s[i][j]=='1'){
                oo++;
                U.uu(i,j+n);
            }
        }
        bool used[100]={};
        int base=0,one=0;
        dn=0;
        REP(i,n){
            if(used[i])continue;
            PII me=MP(0,0);
            REP(j,n+n){
                if(U.find(j)==U.find(i)){
                    used[j]=1;
                    if(j<n)me.F++;
                    else me.S++;
                }
            }
            if(me.F==me.S){
                base+=me.F*me.S;
                continue;
            }
            else if(me.F+me.S==1){
                one++;
                continue;
            }
            dd[dn++]=me;
        }
        sum[0]=MP(0,0);
        {
            int it=0;
            REPP(i,1,1<<dn){
                if(!(i&(i-1))){
                    sum[i]=dd[it++];
                }
                else{
                    int you=i&-i;
                    sum[i]=MP(sum[you].F+sum[i-you].F,sum[you].S+sum[i-you].S);
                }
            }
        }
        MS1(dp);
        dp[0][0]=0;
        REP(i,1<<dn){
            REP(j,one+1){
                if(dp[i][j]==-1)continue;
                int re=(1<<dn)-1-i;
                for(int k=re;k;k=(k-1)&re){
                    int need=max(0,sum[k].S-sum[k].F);
                    if(j+need<=one)mii(dp[i|k][j+need],dp[i][j]+sqr(max(sum[k].F,sum[k].S)));
                }
            }
        }
        int an=INF;
        REP(i,one+1){
            if(dp[(1<<dn)-1][i]==-1)continue;
            an=min(an,base+dp[(1<<dn)-1][i]+(one-i));
        }
        printf("Case #%d: %d\n",case_n++,an-oo);
    }
    return 0;
}
