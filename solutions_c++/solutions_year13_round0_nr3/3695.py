#include <iostream>

using namespace std;

int main() {
  int T, A, B, count;
  
  cin >> T;
  
  for (int i = 0; i < T; ++i) {
    cin >> A >> B;
    
    cout << "Case #" << i + 1 << ": ";
    
    count = 0;
    
    if ( A <= 1 && 1 <=B )
      ++count;
    if ( A <= 4 && 4 <=B )
      ++count;
    if ( A <= 9 && 9 <=B )
      ++count;
    if ( A <= 121 && 121 <=B )
      ++count;
    if ( A <= 484 && 484 <=B )
      ++count;
  
    cout << count << endl;
  }
   
}