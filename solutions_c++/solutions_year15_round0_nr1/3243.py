#include<iostream>

#include<string>

#include<vector>

using namespace std;

int main(){
   int n;
   int m;
   cin >> n;
   for(int t=1;t<=n;t++){
      string shyness;
      cin >> m;
      cin >> shyness;
      cout << "Case #" << t << ": ";
      int standing = 0;
      int required = 0;
      standing = shyness[0]-'0';
      int p;
      for(int i=1;i<=m;i++){
         p = shyness[i]-'0';
         if(p == 0) continue;
         if(standing < i){
            // cout << "i:" << i << " hire: " << i - standing << '\n';
            required += i - standing;
            standing += i - standing;
         }
         standing += p;
      }
      cout << required;
      cout << "\n";
   }

   return 0;
}
