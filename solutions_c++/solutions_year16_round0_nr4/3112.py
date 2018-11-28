/*
	Alexandre Borgo - Google Code Jam - 2016 - D. Fractiles
*/

#include <iostream>

using namespace std;

int main() {
    int T;
    int K;
    int C;
    int S;

    cin >> T;

    for(int i = 1 ; i <= T ; i++) {
    cin >> K;
    cin >> C;
    cin >> S;

    if(K != S) {
        cout << "Case #" << i << ": " << "IMPOSSIBLE";
    }
    else {
        cout << "Case #" << i << ":";

        for(int j = 1 ; j <= S ; j++) {
            cout << " " << j;
        }
    }

    cout << endl;
  }

  return 0;
}
