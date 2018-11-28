#include <iostream>
using namespace std;

int main() {
  int I;

  cin >> I;
  for (int i=1;i<=I;i++) {
    int K;
    int C;
    int S;

    cin >> K;
    cin >> C;
    cin >> S;

    cout << "Case #"<<i<<":";
    for (int j=1;j<=S;j++) {
      cout << " " << j;
    }
    cout << endl;
    // S=K... just look at the first K blocks.
  }
}
