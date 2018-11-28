#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,cases;
    double c,f,x,v1,v2,init,farmc;
    scanf("%d",&t);
    cases=0;
    while(cases++ < t)
    {
              scanf("%lf%lf%lf",&c,&f,&x);

              init=2.0;
              v2=x/init;
              farmc=c/init;

              do
              {
                   v1=v2;
                   init+=f;
                   v2=x/init;
                   v2+=farmc;
                   farmc+=c/init;
                   
              }while(v2<v1);
              printf("Case #%d: %.7lf\n",cases,v1);
    }

    return 0;
}
