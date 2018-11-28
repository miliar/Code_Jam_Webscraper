#include<bits/stdc++.h>
using namespace std;
int main(){
   int test,ans,t=0;;
   cin >> test;
   while(test--){
      int x,r,c;
      cin >> x >> r >> c;
      if(x==1) ans =2;
      else if(x==2){
         if((r*c)%2 ==0) ans =2;
         else ans =1;
      }
      else if(x==3){
         if(r<3 && c<3) ans = 1;
         else{
            if(r*c == 3) ans =1;
            else if((r*c)%3 ==0) ans =2;
            else ans=1;
         }
      }
      else{
         if(r<4 && c<4) ans =1;
         else{
            if(r*c ==4 || r*c ==8) ans =1;
            else ans =2;
         }
      }
      cout << "Case #" << ++t << ": " ;
      if(ans==1) cout << "RICHARD\n";
      else cout << "GABRIEL\n";
   }
}
