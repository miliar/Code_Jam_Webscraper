#include <iostream>
#include <string>

using namespace std;

int main ()
  {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
      { 
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << t << ": 1";
        for (int i = 2; i <= K; ++i) cout << " " << i;
        cout << "\n";
      }
    return 0;
  }
