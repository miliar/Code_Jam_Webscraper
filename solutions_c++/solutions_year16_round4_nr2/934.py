#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<list>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define FIT(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)
#define CLR(i) memset(i,0,sizeof(i))
#define eps (1e-8)
#define feq(x,y) (fabs((x)-(y))<=eps)
#define fgt(x,y) (((x)-(y)) > eps)
#define flt(x,y) (((y)-(x)) > eps)
#define fgeq(x,y) (fgt(x,y) || feq(x,y))
#define fleq(x,y) (flt(x,y) || feq(x,y))
#define ll long long

int T,K,N;
double P[300];
bool ok[300];
bool yes[300];
double ans;
double tans;

void calc(int pos,int cnt){
    if (pos == N){
        if (cnt != (K/2)) return;
        double tmp = 1.0;
        FOR(i,0,N){
            if (!ok[i]) continue;
            if (yes[i]) tmp *= P[i];
            else tmp *= (1.0-P[i]);
        }
        tans += tmp;
        return;
    }
    
    if (!ok[pos]){
        calc(pos+1,cnt);
        return;
    }
    yes[pos] = 1;
    calc(pos+1,cnt+1);
    yes[pos] = 0;
    calc(pos+1,cnt);
}

void f(int pos,int cnt){
    if (pos == N){
        if (cnt != K) return;

        CLR(yes);
        tans = 0.0;
        calc(0,0);
        ans = max(ans, tans);
        return;
    }
    
    ok[pos] = 1;
    f(pos+1,cnt+1);
    ok[pos] = 0;
    f(pos+1,cnt);
}

int main(){
    scanf("%d",&T);
    FOE(t,1,T){
        scanf("%d%d",&N,&K);
        FOR(i,0,N) scanf("%lf",&P[i]);
        ans = 0.0;
        f(0,0);
        printf("Case #%d: %.9lf\n",t,ans);
    }

    return 0;
}
