#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
   int t;
   cin >> t;
   for(int z = 1; z<=t; z++) {
      string s;
      int n;
      cin >> n;
      cin >>s;
      vector<int> v(n+1);
      v[0] = s[0]-'0';
      for(int i = 1; i<=n; i++) {
         v[i] = v[i-1] + s[i]-'0';
      }
      int inv = 0;
      for(int i = 1; i<=n; i++) {
         if(v[i-1] < i) {
            
            inv += i-v[i-1];
            for(int k = i; k<=n; k++) {
               v[k] += i-v[i-1];
            }
         }
      }
      cout << "Case #" << z << ": " << inv << '\n';
   }
}