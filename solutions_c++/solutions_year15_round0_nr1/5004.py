#include <iostream>
#include <cstring>

using namespace std;

int main()
{
     freopen("vats.txt", "r", stdin);
     freopen("op.txt", "w", stdout);
    
     int test;
     cin>>test;
     int cc = 0;
     while (test--){
           int n;
           cin>>n;
           string s;
           cin>>s;
           int ans = 0;
           int cur = 0;
           for (int i=0;i<s.size();i++){
               if (s[i] != '0'){
                  if (cur >= i){
                     cur += s[i] - '0';
                  } else {
                     int temp = abs(i - cur);
                     ans += temp;
                     cur += temp;
                     cur += s[i] - '0';
                  }
               } 
           }
           cc++;
           cout<<"Case #"<<cc<<": ";
           cout<<ans<<"\n";
     }     
     return 0;
}
