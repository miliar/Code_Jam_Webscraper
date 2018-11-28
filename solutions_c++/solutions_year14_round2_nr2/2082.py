#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <algorithm>
#include <cmath>
#include <set>


using namespace std;




int winning(int A, int B, int K) {
  int win = 0;
  for (int a = 0; a < A; ++a){
    for (int b = 0; b < B; ++ b){
      if ((a & b) < K) ++win;
    }
  }
  return win;
}




int main() {
  ios_base::sync_with_stdio(false);
  
  int T;
  cin >> T;

  for (int t=1; t<=T; ++t) {
    int A, B, K;
    cin >> A >> B >> K;
    
    cout << "Case #" << t << ": " << winning(A, B, K) << '\n';
  }

  
  return 0;
}
