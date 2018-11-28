#include<iostream>
#include<stdio.h>
#include<math.h>

using namespace std;

int main(){

   int t;
   cin>>t;
   for(int i=1;i<=t;i++){
       double c,f,x;
       cin>>c>>f>>x;
       int k = floor((x/c - 2/f));
       double time = 0;
       for(int j=0;j<k;j++){
           time = time + c / (2 +j*f);
       }
       if( k <= 0)
       k = 0;
       time = time + x / (2 + f * k);
       cout<<"Case #"<<i<<": ";
       printf("%.7lf\n",time);
   }

}
