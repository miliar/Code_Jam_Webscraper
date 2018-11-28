#include<stdio.h>
long i,j,k,t,n,o,a[1002],M,r,R,z,h;
int main(){
 scanf("%ld",&t);
 for(o=1;o<=t;o++){
  scanf("%ld",&n);
  for(M=0,i=0;i<n;i++){ scanf("%ld",&a[i]); if(a[i]>M) M=a[i]; }
  
  R=M;
  for(h=M;h>0;h--){
  
   for(i=0,r=0,k=0;i<n;i++){
    r+=(a[i]-1)/h;
   }
   if(r+h<R) R=r+h;
  
  }
  
  printf("Case #%ld: %ld\n",o,R);
  
 }
}
