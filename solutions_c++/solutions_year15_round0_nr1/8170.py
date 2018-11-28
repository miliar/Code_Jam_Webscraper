#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define LL long long

int main() { 
   int t;
   cin>>t;
   for(int tc = 1;tc <= t; tc++) {      
      int smax; cin>>smax;
      int arr[smax + 1];
      char ch;
      LL friends = 0;
      for(int i = 0; i <= smax; i++) {
         cin>>ch;
         arr[i] = ch - '0';
      }
      
      LL sum = 0; 
       
      for(int i = 0;i < smax + 1;i++) {
         if(sum >= i) {
            sum += arr[i];
         }       
         else { 
            friends += (i - sum);
            sum += (arr[i] + (i - sum));
         }
      }
      cout<<"Case #"<<tc<<": "<<friends<<endl; 
   }
   return 0;               
}
       
