#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T, K, C, S, i;
  cin >> T;
  i = T;
  while(T > 0) {
    cout << "Case #" << i - T + 1 << ":"; 
    cin >> K >> C >> S;
    for(int j = 1; j <= S; ++j)
      cout << ' ' << j;
    cout << endl;
    T--;
  } 
  return 0;
}
