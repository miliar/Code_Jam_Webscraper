#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
typedef unsigned long long  LL;
using namespace std ;
typedef pair<int,int> PII;

double C,F,X;

double gao(int N){
    double res=0;
    for (int i=1;i<=N;i++) res+=C/(2.0+(i-1)*F);
    res+=X/(2.0+N*F);
    return res;
}

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int _,k;
    scanf("%d",&_);
    for (k=1;k<=_;k++){
        scanf("%lf%lf%lf",&C,&F,&X);
        int l=0,r=200000;
        while (r-l>5){
            int x=l+r>>1,y=x+1;
            if (gao(x)-gao(y)>1e-8) l=x+1;
            else r=y;
        }
        double ans=1e300;
        for (int i=l;i<=r;i++) ans=min(ans,gao(i));
        printf("Case #%d: %.7f\n",k,ans);
    }
}
