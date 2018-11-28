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
char s[SIZE][SIZE];
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};
int n,m;
bool Out(int x,int y){return x<0||y<0||x>=n||y>=m;}
char dir[10]="v>^<";
int main(){
    CASET{
        RII(n,m);
        REP(i,n)RS(s[i]);
        int an=0;
        REP(i,n){
            REP(j,m){
                if(s[i][j]!='.'){
                    bool can=0;
                    REP(k,4){
                        int x=i;
                        int y=j;
                        bool v=0;
                        for(x+=dx[k],y+=dy[k];!Out(x,y);x+=dx[k],y+=dy[k]){
                            if(s[x][y]!='.'){
                                v=1;
                                break;
                            }
                        }
                        if(!v&&s[i][j]==dir[k]){
                            an++;
                        }
                        if(v)can=1;
                    }
                    if(!can){
                        an=-1;
                    }
                }
                if(an==-1)break;
            }
            if(an==-1)break;
        }
        if(an!=-1)
            printf("Case #%d: %d\n",case_n++,an);
        else
            printf("Case #%d: IMPOSSIBLE\n",case_n++);
    }
    return 0;
}
