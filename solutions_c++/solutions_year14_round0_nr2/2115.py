#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int cases=1,t;
    double c,f,x,time,current_rate=0;
    scanf("%d",&t);
    while(cases<=t){
        scanf("%lf%lf%lf",&c,&f,&x);
        current_rate=2;
        time=0;
        while((x/current_rate)>((x/(current_rate+f))+(c/(current_rate)))){
            time+=c/current_rate;
            current_rate+=f;
        }
        time+=x/current_rate;
        printf("Case #%d: %.7f\n",cases,time);
        cases++;
    }
    return 0;
}

