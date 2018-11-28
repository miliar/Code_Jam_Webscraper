#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <string.h>
using namespace std;
int main(){
  freopen("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int uu=0;uu<t;uu++){
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double t = 0;
        double cc = 2.0;
        while((x/cc)>((c/cc)+(x/(cc+f)))){
            t+= (c/cc);
            cc = cc+f;
        }
        t += (x/cc);
        printf("Case #%d: %lf\n",uu+1,t);
    }
    return 0;
}
