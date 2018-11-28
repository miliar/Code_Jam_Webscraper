//Joe Snider
//4/16
//
//codejam qual 2016, d (fractiles)

#include <iostream>

using namespace std;

int main() {
   int T, K, C, S;
   cin >> T;
   for(int c = 1; c <= T; ++c) {
      //for the small dataset with S=K, always just check the first S (10 cheap points)
      cin >> K >> C >> S;
      cout << "Case #" << c << ": ";
      for(int i = 1; i <= S-1; ++i) {
         cout << i << " ";
      }
      cout << S << "\n";
   }
   
   return 0;
}
