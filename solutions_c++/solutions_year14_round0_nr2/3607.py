#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std; 



int T;

double c,f,x;

int main(){
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
        scanf("%lf %lf %lf",&c,&f,&x);
        double current_rate=2.0;
        double res=0.0;
        while (true){
              double time_without_building= x/current_rate;
              double time_with_building = c/current_rate + x/(current_rate+f);
              if (time_without_building<time_with_building){
                 res=res+time_without_building;
                 break;                                           
                 }
              res=res+c/current_rate;   
              current_rate=current_rate+f;    
              }
        printf("Case #%d: %.7f\n",t,res);
        }
    return 0;
    }
