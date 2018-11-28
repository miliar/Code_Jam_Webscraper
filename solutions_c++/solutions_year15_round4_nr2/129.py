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
const double EPS = 1e-5;
double C[SIZE],R[SIZE];
int ng(double x){
    if(x>0)return 1;
    return -1;
}
int main(){
    CASET{
        int n;
        double V,X;
        scanf("%d%lf%lf",&n,&V,&X);
        REP(i,n){
            double x,y;
            scanf("%lf%lf",&x,&y);
            R[i]=x;
            C[i]=y;
        }
        double ll=0,rr=1e7;
            double mi=1e9;
        REP(k,80){
            bool suc=0;
            double mm=(ll+rr)*0.5;
            REP(i,n){
                if(fabs(X-C[i])<EPS){
                    if(mm*R[i]>=V){
                        suc=1;
                        break;
                    }
                }
            }
            if(!suc){
                REP(i,n){
                    if(fabs(X-C[i])<EPS)continue;
                    REPP(j,i+1,n){
                        if(fabs(X-C[j])<EPS)continue;
                        if(ng(X-C[i])*ng(X-C[j])<0){
                            double v1=(C[j]-X)/(C[j]-C[i]);
                            double v2=1-v1;
                            double v3=max(v1/R[i],v2/R[j]);
                            double need=v3*V;
                            mi=min(mi,need);
                            if(need<=mm){
                                suc=1;
                            }
                        }
                    }
                }
            }
            if(suc)rr=mm;
            else ll=mm;
        }
        printf("Case #%d: ",case_n++);
        if(ll>5e6)puts("IMPOSSIBLE");
        else printf("%.9f\n",(ll+rr)*0.5);
    }
    return 0;
}
