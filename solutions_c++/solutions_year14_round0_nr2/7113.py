#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
    int t;
    freopen("B-large.in", "r", stdin);
    freopen("large.txt", "w", stdout);
    scanf("%d\n",&t);
    for(int tc = 1; tc <= t; tc++){
        printf("Case #%d: ", tc);
        double c,f,x,iter;
        scanf("%lf %lf %lf",&c,&f,&x);
        double newiter = x/2.0;
        int it=0;
        do{
              iter = newiter;
              it++;
              newiter = iter - (x/ (2.0+ f*(it-1) ) ) + c/(2+f*(it-1)) + x/( 2.0+ (f*it) ) ;
          }while(newiter<iter);
        printf("%lf\n", iter);
}



    return 0;
}

