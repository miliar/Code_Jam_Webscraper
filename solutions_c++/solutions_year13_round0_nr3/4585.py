#include<stdio.h>

int main(){
 int t,n,c,q,l,r,i,j,b=0;//,A[100]={0};
 scanf("%d",&t);
 while(t--){
   //A[b]=0;
   scanf("%d %d %d", &n, &c, &q);
   //c--;
   b=c;
   while(q--){
     scanf("%d %d", &l, &r);
     //l--; r--;
     if(l<=b && b<=r){
       //printf("%d-(%d-%d)",r,b,l);
       b=r-(b-l);
     }
     //printf("\ncheck: b=%d, l=%d, r=%d",b,l,r);
   }
   printf("%d",b);
 }
return 0;
}
