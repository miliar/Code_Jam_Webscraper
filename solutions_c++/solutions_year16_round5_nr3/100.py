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
typedef long long LL;
using namespace std;
const int MOD = 1e9+7;
const int SIZE = 1e3+5;
const double INF = 1e18;
const double EPS = 1e-9;
struct PP{
    int x,y,z;
    int v_x,v_y,v_z;
}p[SIZE];
int N,S;
struct data{
    double lo,hi;
    int y;
    data(double _lo=0,double _hi=0,int _y=0):lo(_lo),hi(_hi),y(_y){}
    bool operator<(const data& b)const{
        return lo<b.lo;
    }
};
vector<data>time_seg[SIZE];
int it[SIZE];
double sqr(double x){return x*x;}
bool get(PP& X,PP& Y,double& lo,double& hi,double limit){
    double aa=sqr(X.v_x-Y.v_x)+sqr(X.v_y-Y.v_y)+sqr(X.v_z-Y.v_z);
    double bb=2*((X.v_x-Y.v_x)*(X.x-Y.x)+(X.v_y-Y.v_y)*(X.y-Y.y)+(X.v_z-Y.v_z)*(X.z-Y.z));
    double cc=sqr(X.x-Y.x)+sqr(X.y-Y.y)+sqr(X.z-Y.z)-sqr(limit);
    if(aa<EPS){
        if(cc>=0)return 0;
        lo=0,hi=INF;
        return 1;
    }
    double delta=sqr(bb)-4*aa*cc;
    if(delta<=0)return 0;
    else{
        double v2=(-bb+sqrt(delta))/(2*aa);
        if(v2<0)return 0;
        double v1=(-bb-sqrt(delta))/(2*aa);
        lo=max(0.,v1);
        hi=min(v2,INF);
    }
    return 1;
}
void rev(double& v){
    v=-v;
}
bool suc(double limit){
    REP(i,N)time_seg[i].clear();
    MS0(it);
    REP(i,N){
        REP(j,i){
            data me;
            if(get(p[i],p[j],me.lo,me.hi,limit)){
                me.y=j;
                time_seg[i].PB(me);
                me.y=i;
                time_seg[j].PB(me);
            }
        }
    }
    REP(i,N)sort(ALL(time_seg[i]));
    priority_queue<data>heap;
    while(it[0]<SZ(time_seg[0])&&time_seg[0][it[0]].lo<=S){
        if(time_seg[0][it[0]].y==1)return 1;
        rev(time_seg[0][it[0]].lo);
        heap.push(time_seg[0][it[0]]);
        it[0]++;
    }
    while(!heap.empty()){
        data me=heap.top();heap.pop();
        int id=me.y;
        while(it[id]<SZ(time_seg[id])&&time_seg[id][it[id]].lo<=me.hi+S){
            if(time_seg[id][it[id]].y==1)return 1;
            rev(time_seg[id][it[id]].lo);
            heap.push(time_seg[id][it[id]]);
            it[id]++;
        }
    }
    return 0;
}
int main(){
    CASET{
        RII(N,S);
        REP(i,N){
            RIII(p[i].x,p[i].y,p[i].z);
            RIII(p[i].v_x,p[i].v_y,p[i].v_z);
        }
        double ll=0,rr=2e5;
        REP(k,40){
            double mm=(ll+rr)*0.5;
            if(suc(mm))rr=mm;
            else ll=mm;
        }
        printf("Case #%d: %.7f\n",case_n++,(ll+rr)*0.5);
    }
    return 0;
}
