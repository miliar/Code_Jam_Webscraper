#include<stdio.h>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int main(){
    int ca; scanf("%d",&ca);
    FOE(tt,1,ca){
        double C, F, X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double tu = 0;
        double ans = 1e30;
        FOR(t,0,int((X/C)+1)){
            double speed = 2 + t*F;
            ans = min(ans , tu + X / speed);
            tu += C / speed;
        }
        printf("Case #%d: %f\n", tt, ans);
    }
    return 0;
}
