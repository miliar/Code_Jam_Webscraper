#include <iostream>
#include <string.h>
using namespace std;

long count(long n){

 bool store[10];
 int i,counter=0,j=0;
 long m;

 memset(store,false,sizeof(store));

// if(n==0)
//   return -1;

 while(counter < 10){
   m = n*(j+1);
//   cout<<"    "<<m<<endl;
   for(i=0;m!=0;++i){
     if(!store[m%10]){
       ++counter;
       store[m%10]=true;
       if(counter == 10)
         return n*(j+1);
     }
     m/=10;
   }
   ++j;
   if(j>=100)
     return -1;
 }
}

int main(){

 int i,t;
 long n;

 cin>>t;
 for(i=1;i<=t;++i){
   cin>>n;

   long d = count(n);
 
   if(d==-1){
     cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
   } else {
     cout<<"Case #"<<i<<": "<<d<<endl;
   }
 }

 return 0;
}
