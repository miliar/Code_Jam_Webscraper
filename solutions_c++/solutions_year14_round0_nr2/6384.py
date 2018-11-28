/**
   author:liuwen
*/
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("outBig.txt","w",stdout);
    double C,F,X;
    int T,cas=0;scanf("%d",&T);
    while(T--){
        scanf("%lf%lf%lf",&C,&F,&X);
        double t0=0,t1=0,t2=0,S=2;
        for(;;){
            t1=t0+C/S+X/(S+F);
            t2=t0+X/S;
            if(t1>=t2)  break;
            else{
                t0=t0+C/S;
                S=S+F;
            }
        }
        printf("Case #%d: %.7f\n",++cas,t2);
    }
    return 0;
}
