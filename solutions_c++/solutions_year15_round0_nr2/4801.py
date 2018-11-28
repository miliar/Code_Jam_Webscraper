#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;
int main(){
long t,n,d,max,i;
scanf("%ld",&t);
long c=0;
while(t--){
   ++c;
   n=0;
   max=-1;
   scanf("%ld",&d);
   long a[100000];
   for(i=0;i<d;i++){
    scanf("%ld",&a[i]);
    if(max<a[i])
	max=a[i];
   }
   long curr=max,add=0;
   while(max>1){
   for(i=0;i<d;i++){
    if(a[i]==max){
        a[i]=max/2;
        a[d+n]=max-a[i];
        n++;
        add++;
    }
   }
   d=d+n;
   max=-1;
   for(i=0;i<d;i++){
   if(max<a[i])
   max=a[i];
   }
   if(max+add<=curr)
   curr=max+add;
   else 
   break;
   }
   printf("Case #%ld: %ld\n",c,curr);
}
return 0;
}
