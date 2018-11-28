#include <cstdio>
#include <iostream>
using namespace std;

string res(int x, int r, int c){
   if(x>=7)
      return "RICHARD";
   if((r*c)%x!=0)
      return "RICHARD";
   if(x==2)
      return "GABRIEL";
   if(r<=x/2 || c<=x/2)
      return "RICHARD";
   return "GABRIEL";

   
}

int main(){

   int nbTests;
   scanf("%d", &nbTests);
   for(int i=1; i<=nbTests; i++){
      int x,r,c;
      scanf("%d%d%d", &x,&r,&c);
      cout<<"Case #"<<i<<": "<<res(x,r,c)<<"\n";
   }

}