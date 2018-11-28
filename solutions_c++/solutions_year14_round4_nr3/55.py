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
const int SIZE = 1010;
int xx1[SIZE],xx2[SIZE],yy1[SIZE],yy2[SIZE];
vector<pair<int,int> >e[SIZE];
bool XX(int r1,int r2,int r3,int r4){
    if(r2<r3||r4<r1)return false;
    return true;
}
int dis(int id1,int id2){
    int mi=1e9;
    if(XX(xx1[id1],xx2[id1],xx1[id2],xx2[id2])){
        mi=min(mi,abs(yy1[id1]-yy2[id2]));
        mi=min(mi,abs(yy1[id2]-yy2[id1]));
    }
    if(XX(yy1[id1],yy2[id1],yy1[id2],yy2[id2])){
        mi=min(mi,abs(xx1[id1]-xx2[id2]));
        mi=min(mi,abs(xx1[id2]-xx2[id1]));
    }
    int mi1=abs(xx1[id1]-xx1[id2]);
    mi1=min(mi1,abs(xx1[id1]-xx2[id2]));
    mi1=min(mi1,abs(xx2[id1]-xx1[id2]));
    mi1=min(mi1,abs(xx2[id1]-xx2[id2]));
    
    int mi2=abs(yy1[id1]-yy1[id2]);
    mi2=min(mi2,abs(yy1[id1]-yy2[id2]));
    mi2=min(mi2,abs(yy2[id1]-yy1[id2]));
    mi2=min(mi2,abs(yy2[id1]-yy2[id2]));
    mi=min(mi,max(mi1,mi2));
    return mi;
}
int used[SIZE],v[SIZE];
int go(int N){
    queue<int>qq;
    REP(i,SIZE)v[i]=1e9;
    v[0]=0;
    qq.push(0);
    MS0(used);
    while(SZ(qq)){
        int x=qq.front();
        qq.pop();
        used[x]=0;
        REP(i,SZ(e[x])){
            int y=e[x][i].F;
            if(v[y]>v[x]+e[x][i].S){
                v[y]=v[x]+e[x][i].S;
                if(!used[y]){
                    used[y]=1;
                    qq.push(y);
                }
            }
        }
    }
    return v[N];
}
int main(){
    CASET{
        DRIII(W,H,B);
        REP(i,SIZE)e[i].clear();
        REP(i,B){
            RII(xx1[i+1],yy1[i+1]);
            RII(xx2[i+1],yy2[i+1]);
            xx2[i+1]++;
            yy2[i+1]++;
        }
        e[0].PB(MP(B+1,W));
        REP(i,B){
            e[0].PB(MP(i+1,xx1[i+1]));
            REP(j,B){
                if(i==j)continue;
                e[i+1].PB(MP(j+1,dis(i+1,j+1)));
            }
            e[i+1].PB(MP(B+1,W-xx2[i+1]));
        }
        printf("Case #%d: %d\n",case_n++,go(B+1));
    }
    return 0;
}
