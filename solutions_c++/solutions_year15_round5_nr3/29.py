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
double an;
// template end here
int Y,N,P[SIZE],S[SIZE];
set<int>L,R;
void dfs(double pos,double t){
    if(!SZ(R)){
        double now=t;
        for(set<int>::iterator it=L.begin();it!=L.end();it++){
            now=max(now,(pos-(P[*it]-t*S[*it]))/(Y-S[*it]));
        }
        an=min(an,t+now);
        return;
    }
    if(!SZ(L)){
        double now=t;
        for(set<int>::iterator it=R.begin();it!=R.end();it++){
            now=max(now,((P[*it]+t*S[*it])-pos)/(Y-S[*it]));
        }
        an=min(an,t+now);
        return;
    }
    double mi=1e27;
    int id=-1;
    for(set<int>::iterator it=L.begin();it!=L.end();it++){
        double v=(pos-(P[*it]-t*S[*it]))/(Y-S[*it]);
        if(v<mi){
            mi=v;
            id=*it;
        }
    }
    L.erase(id);
    dfs(pos-mi*Y,t+mi);
    L.insert(id);

    mi=1e27;
    id=-1;
    for(set<int>::iterator it=R.begin();it!=R.end();it++){
        double v=((P[*it]+t*S[*it])-pos)/(Y-S[*it]);
        if(v<mi){
            mi=v;
            id=*it;
        }
    }
    R.erase(id);
    dfs(pos+mi*Y,t+mi);
    R.insert(id);

}
int main(){
    CASET{
        an=1e27;
        RII(Y,N);
        L.clear();R.clear();
        REP(i,N){
            RI(P[i]);
        }
        REP(i,N)RI(S[i]);
        REP(i,N){
            if(P[i]<0)L.insert(i);
            else R.insert(i);
        }
        dfs(0,0);
        printf("Case #%d: %.12f\n",case_n++,an);
    }
    return 0;
}
