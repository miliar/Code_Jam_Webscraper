#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
using namespace std;
int main(){
 const double PI=asin(1)*2;
 int ntc=0;
 cin>>ntc;
 cin.get();
 for(int tc=1;tc<=ntc;++tc) {
   long long r,t;
   cin>>r>>t;
   cin.get();
   long long ans=0;
   long long s=0;
   while(t>s) {
     s=ans*(1+2*r+2*(ans-1));
     ans++;
   }
   cout<<"Case #"<<tc<<": ";
   if(t==s) {
     cout<<ans-1;
   } else {
     cout<<ans-2;
   }
   cout<<endl;
 }
 return 0;
}
