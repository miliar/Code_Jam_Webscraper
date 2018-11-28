#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <fstream>
#include <map>
#include <utility>
#include <vector>
using namespace std;

double calcu( double c,  double currentRate,  double f, double x){
    double totalTime = 0;
    while(1){
        if(x/currentRate < c/currentRate + x/(currentRate+f)){
            totalTime += x/currentRate;
            return totalTime;
        }
        totalTime += c/currentRate;
        currentRate += f;
    }
}

int main(){

    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1; t<=T; t++){
        double c, currentRate, f, x, ans;
        scanf("%lf%lf%lf",&c,&f,&x);
        currentRate = 2.0;
        ans = calcu(c,currentRate,f,x);
        printf("Case #%d: %.7lf\n",t,ans);
        //__mingw_printf("Case #%d: %lf\n",t,ans);
    }


return 0;
}
