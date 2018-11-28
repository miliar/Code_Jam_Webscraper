#include <stdio.h>
FILE *fp;
int a[10]={1,2,4,8,16,32,64,128,256,512};
int bein(long long n);
long long gcd(long long a,long long b);

int main(){
     int t,ri; 
     long long p,q,x,i,ch,j;
     fp=fopen("A_large.out","w");
     scanf("%d",&t);
     for (ri=1;ri<=t;ri++){
         scanf("%lld%c%lld",&p,&ch,&q);
         fprintf(fp,"Case #%d: ",ri);
         x=gcd(p,q);
         p/=x;
         q/=x;
         if (bein(q)==0) fprintf(fp,"impossible\n");
         else {
              i=0;
              j=1;
              while (p*j<q){
                    i++;
                    j*=2;
              }
              fprintf(fp,"%d\n",i);
          }
     }
     return 0;
} 
         
int bein(long long n){
    long long i;
    i=1;
    while (i<n) i*=2;
    if (n==i) return 1;
    return 0;
}

long long gcd(long long a,long long b)
{
     if (a%b==0) return b;
     else return gcd(b,a%b);
}
