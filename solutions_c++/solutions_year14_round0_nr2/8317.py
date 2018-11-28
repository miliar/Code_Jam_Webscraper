#include <stdio.h>

long n, i, v, j, t, k, p, y, b;
double c, f, x, m=-1, s=2, s1;;

int main(){
    freopen("B-large.in", "r", stdin);
	freopen("cookie.out", "w", stdout);
   scanf("%ld", &t);
   for(k=1; k<=t; k++){
      s1=0;
      s=2;
      scanf("%lf%lf%lf", &c, &f, &x);
      m=x/s;
      while(t){
        s1+=c/s;
        s+=f;
        if(s1+x/s<m)
           m=s1+x/s;
        else break;
      }
        printf("Case #%ld: %.7lf\n", k, m);


   }
}
