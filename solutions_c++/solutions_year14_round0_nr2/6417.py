#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    
    int n,i,j,k,z,t;
    double sum,c,f,x,p;
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    scanf("%d",&t);
    
    for(z=1;z<=t;z++)
       {
        
        scanf("%lf %lf %lf",&c,&f,&x);
        
        sum =0;
        p=2;
        while(c/p + x/(p+f) < x/p)
           {
            sum += c/p;
            p+=f;
         //   printf("p = %.1lf   sum = %.3lf\n",p,sum);
           }
        sum += x/p;
        printf("Case #%d: %.7lf\n",z,sum);
        
       }
    
    
    
 scanf(" ");
 return 0;
}
