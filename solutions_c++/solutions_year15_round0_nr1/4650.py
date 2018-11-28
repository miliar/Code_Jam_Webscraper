#include<bits/stdc++.h>
using namespace std;
int main(){
   int test,n,t=0;
   string str;
   cin >> test;
   while(test--){
      cin >> n >> str;
      int cnt=str[0]-48,ans=0;
      for(int i=1;i<=n;i++){
         if(str[i]!='0' && i> cnt){
            ans += i-cnt;
            cnt = i;
         }
         cnt += str[i]-48;
      }
      cout << "Case #" << ++t << ": " << ans << "\n";
   }
}
