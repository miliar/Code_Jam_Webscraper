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
const int ROUND = 5e3;
const int SIZE = 1e2+10;
VI e[SIZE];
int pre[SIZE];
long double dp[SIZE],C[SIZE][SIZE];
int num[SIZE];
void pree(){
    REP(i,SIZE){
        C[i][0]=1;
        REPP(j,1,i+1)C[i][j]=C[i-1][j-1]+C[i-1][j];
    }
}
void dfs(int x){
    num[x]=0;
    if(!SZ(e[x])){
        dp[x]=1;
        num[x]=1;
        return;
    }
    REP(i,SZ(e[x])){
        int y=e[x][i];
        dfs(y);
        dp[x]*=C[num[x]+num[y]][num[y]];
        num[x]+=num[y];
    }
    num[x]++;
}
mt19937 rng(0x5EED);
int randint(int lb, int ub) {
    return uniform_int_distribution<int>(lb, ub)(rng);
}
bool same(char s1[],char s2[],int n){
    REP(i,n){
        if(s1[i]!=s2[i])return 0;
    }
    return 1;
}
int used[SIZE],tt;
char c[SIZE];
int main(){
    pree();
    CASET{
        DRI(N);
        MS0(num);
        REP(i,N+1)e[i].clear();
        REP(i,N){
            DRI(x);
            pre[i+1]=x;
            e[x].PB(i+1);
        }
        c[0]='a';
        RS(c+1);
        dfs(0);
        printf("Case #%d:",case_n++);
        DRI(Q);
        while(Q--){
            char input[25];
            char s[111];
            RS(input);
            int m=LEN(input);
            if(m>N){
                printf(" 0.00000");
                continue;
            }
            int suc=0;
            REP(k,ROUND){
                set<int>P;
                tt++;
                used[0]=tt;
                REPP(i,1,N+1){
                    P.insert(i);
                }
                REP(i,N){
                    double sum=N-i;
                    double me=randint(0,(int)1e9)*1e-9;
                    double now=0;
                    bool res=0;
                    for(set<int>::iterator it=P.begin();it!=P.end();it++){
                        if(used[pre[*it]]!=tt)continue;
                        now+=num[*it];
                        if(me<now*1./sum+1e-9){
                            used[*it]=tt;
                            P.erase(*it);
                            s[i]=c[*it];
                            if(i>=m-1&&same(s+i-m+1,input,m)){
                                suc++;
                                res=1;
                            }
                            break;
                        }
                    }
                    if(res)break;
                }
            }
            printf(" %.5f",suc*1./ROUND);
            fprintf(stderr," %.5f",suc*1./ROUND);
        }
        puts("");
    }
    return 0;
}
