#include <iostream>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <math.h>
#include<map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
using namespace std;
int t ;
double c , x , f;
int main (){
    
    int counter = 1;
    scanf("%d",&t);
    while (t--) {
        scanf("%lf %lf %lf",&c,&f,&x);
        double mx =(x*f-c*2-c*f)/(c*f);
        if(mx<0){
            printf("Case #%d: %.7lf\n",counter,(x/2));
            counter++;
            continue;
        }
        int mx_i = (int) ceil(mx);
        double res =0;
        for (int i =0; i<mx_i; i++) {
            res+= (c/(2+(i*f)));
        }
        res += x/(2+(mx_i*f));
            printf("Case #%d: %.7lf\n",counter,res);
        counter++;
    }
    return 0;
}