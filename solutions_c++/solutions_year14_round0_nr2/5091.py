#include <stdio.h>
#include <math.h>

int main()
{
    int t;
    double n2;
    double c;
    double f;
    double x;
    double f1;
    double f2;
    double ans0;
    double ans1;
    int no = 1;
    double ans;
    
    scanf("%d", &t);
    while(t--) {
               scanf("%lf%lf%lf", &c, &f, &x);
               //ans = 0;
               f1 = 2.0;
               if(x<c) {
                       ans1 = (double)(x/2);
               } else {
                      ans0 = 0;
                      ans1 = x/f1;;
                      while((c/f1 + x/(f1+f))< x/f1)
                      {
                              ans1 = ans0 + c/f1 + x/(f1+f);
                              ans0 += c/f1;
                              f1 = f1+f;    
                      }
               }
               printf("Case #%d: %.7lf\n", no, ans1);
               no++;
    }
    //main();
    return 0;
}
               
    
