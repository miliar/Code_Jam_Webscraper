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
char s[100][100];
bool compare(int id1,int id2){
    return strcmp(s[id1],s[id2])<0;
}
int ma,num,N,M;
int qq[4][8],qn[4],tmp[4][8];
void dfs(int x){
    if(x==M){
        REP(i,N){
            if(qn[i]==0)return;
        }
        memcpy(tmp,qq,sizeof(tmp));
        int now=0;
        REP(i,N){
            now++;
            sort(tmp[i],tmp[i]+qn[i],compare);
            REP(j,qn[i]){
                int k=0;
                if(j){
                    while(s[tmp[i][j]][k]&&s[tmp[i][j]][k]==s[tmp[i][j-1]][k])k++;
                }
                while(s[tmp[i][j]][k]){
                    k++;
                    now++;
                }
            }
        }
        if(now==ma)num++;
        else if(now>ma){
            ma=now;
            num=1;
        }
        return;
    }
    REP(i,N){
        qq[i][qn[i]++]=x;
        dfs(x+1);
        qn[i]--;
    }
}
int main(){
    CASET{
        MS0(qn);
        ma=-1;
        RII(M,N);
        REP(i,M)RS(s[i]);
        dfs(0);
        printf("Case #%d: %d %d\n",case_n++,ma,num);
    }
    return 0;
}
