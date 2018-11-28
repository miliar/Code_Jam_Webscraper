//Lasha Bukhnikashvili
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#define Pi 3.14159265358
#define mod9 %1000000009
#define INF 1000000001
#define mod7 1000000009
#define LL  long long
#define time clock()/(double)CLOCKS_PER_SEC
using namespace std;
 int i,T,id;
 double x,f,c,t,ans,reg;
int main(){
#ifndef ONLINE_JUDGE
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
 #endif
   cin>>T;
   while (T--){
         id++;
         cin>>c>>f>>x;
         double reg=2;
         ans=INF;
         t=0;
         for (i=1;i<=int(x);i++){
             ans=min(ans,t+x/reg);
             t+=c/(reg*1.0);
             reg+=f;
         };
         cout<<"Case #";
         cout<<id;
         cout<<": ";
         cout<<fixed<<setprecision(7)<<ans<<endl;
         
   };
 return 0;
}
 
