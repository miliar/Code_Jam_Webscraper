#include <bits/stdc++.h>
#include <string>
using namespace std;
 int main() {
   int t;
   cin>>t;
   long long int n, m;
   long long int res;
   for(int c=1; c<=t; c++) {
     set<int> dig;
     cin>>n;
     if(n == 0) {cout<<"Case #"<<c<<": INSOMNIA"<<endl;}
     else {
     int x;
     long long int y = 1;
     while(dig.size() != 10) {
       m = n * y; res = m;
       while(m>0) {
         x = m % 10;
         dig.insert(x);
         m /= 10;
       }
       y++;
     }
     cout<<"Case #"<<c<<": "<<res<<endl;
   }
 }

   return 0;
 }
