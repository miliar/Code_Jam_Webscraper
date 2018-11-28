//Joe Snider
//5/14
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//bf
void doit(int A, int B, int K) {
   unsigned long val = 0;
   for(int i = 0; i < A; ++i) {
      for(int j = 0; j < B; ++j) {
         val += ((i&j) < K)?1:0;
         //cout << "gh1 " << i << " " << j << " " << (i&j) << " " << val << " " << K << "\n" << flush;
      }
   }
   cout << val;
}

int main() {
   int T;
   int A, B, K;
   cin >> T;
   for(int t = 1; t <= T; ++t) {
      cin >> A >> B >> K;
      cout << "Case #" << t << ": " << flush;
      doit(A,B,K);
      cout << "\n" << flush;
   }
}