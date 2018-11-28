#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<math.h>
#define pdi pair<double,int>
using namespace std;
int n;
double SS, D[1010][1010], ED[1010][1010];
struct point{
    point(){}
    point(double x_, double y_, double z_){
        x=x_,y=y_,z=z_;
    }
    point operator -(const point &p)const{
        return point(x-p.x,y-p.y,z-p.z);
    }
    point operator +(const point &p)const{
        return point(x+p.x,y+p.y,z+p.z);
    }
    point operator *(const double c)const{
        return point(c*x,c*y,c*z);
    }
    double x, y, z;
}w[1010], V[1010];
priority_queue<pdi>PQ;
double Mul(point a, point b){
    return a.x*b.x+a.y*b.y+a.z*b.z;
}
struct AA{
    double b, e;
    int a;
    AA(){}
    AA(int a_, double b_, double e_){
        a=a_,b=b_,e=e_;
    }
    bool operator<(const AA &p)const{
        return b<p.b;
    }
};
vector<AA>E[1010];
void Ins(int a, int b, point p1, point p2, double MD){
    if(Mul(p2,p2) < 1e-5){
        if(Mul(p1,p1) <= MD*MD){
            E[a].push_back(AA(b,0,1e9));
            E[b].push_back(AA(a,0,1e9));
        }
        return;
    }
    double t = -Mul(p1,p2) / Mul(p2,p2);
    point P = p1 + p2*t;
    if(Mul(P,P)>MD*MD)return;
    double tt = sqrt((MD*MD - Mul(P,P)) / Mul(p2,p2));
    if(tt+t > 0.0){
        E[a].push_back(AA(b,max(0.0,t-tt),t+tt));
        E[b].push_back(AA(a,max(0.0,t-tt),t+tt));
    }
}
void UDT(int a, int b, double t){
    if(D[a][b] <= t)return;
    D[a][b] = t;
    PQ.push(pdi(-t,(a<<10)+b));
}
bool Pos(double MD){
    int i, j;
    for(i=1;i<=n;i++){
        E[i].clear();
    }
    for(i=1;i<=n;i++){
        for(j=i+1;j<=n;j++){
            Ins(i,j,w[j]-w[i],V[j]-V[i],MD);
        }
        sort(E[i].begin(),E[i].end());
        for(j=0;j<E[i].size();j++){
            ED[i][E[i][j].a] = E[i][j].e;
        }
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            D[i][j]=1e9;
        }
    }
    while(!PQ.empty())PQ.pop();
    for(j=0;j<E[1].size();j++){
        if(E[1][j].b <= SS){
            UDT(1,E[1][j].a,E[1][j].b);
        }
    }
    /*if(MD<20 && MD>10){
        for(i=1;i<=n;i++){
            for(j=0;j<E[i].size();j++){
                printf("%d %d %.3lf %.3lf\n",i,E[i][j].a,E[i][j].b,E[i][j].e);
            }
        }
    }*/
    while(!PQ.empty()){
        pdi tp = PQ.top();
        PQ.pop();
        int ee = tp.second&1023;
        double et = ED[tp.second>>10][ee];
        if(ee == 2)return true;
        int tt = lower_bound(E[ee].begin(),E[ee].end(),AA(0,-tp.first,0)) - E[ee].begin();
        for(i=tt;i<E[ee].size();i++){
            if(E[ee][i].b > et + SS)break;
            UDT(ee, E[ee][i].a, max(E[ee][i].b, -tp.first));
        }
    }
    return false;
}
int main(){
    freopen("input.txt","r",stdin);
    FILE *out = fopen("output.txt","w");
    int TC, TT, i, TTT;
    double be, ed, mid;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        fprintf(out,"Case #%d: ",TT);
        printf("%d\n",TT);
        scanf("%d%lf",&n,&SS);
        for(i=1;i<=n;i++){
            scanf("%lf%lf%lf",&w[i].x,&w[i].y,&w[i].z);
            scanf("%lf%lf%lf",&V[i].x,&V[i].y,&V[i].z);
        }
        be = 0.0, ed = 2000.0;
        TTT = 30;
        while(TTT--){
            mid = (be+ed)*0.5;
            if(Pos(mid)){
                ed = mid;
            }
            else be = mid;
        }
        fprintf(out,"%.11lf\n",be);
    }
}
