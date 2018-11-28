#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T, N;
  cin >> T;
  for (int x=1; x<=T; ++x) {
    cin >> N;
    vector<int> input(7, 0);
    vector<int> num(20, 0);

    if (N == 0) {
      cout << "Case #" << x << ": INSOMNIA" << endl;
      continue;
    }
    // parse N to digits
    int k = 0;
    while (N > 0) {
      input[k] = N%10;
      N /= 10;
      ++k;
    }
    int dg = k;
    int counter = 0;
    int state = 0;
    //while (counter < 10) { // TODO
    while (state != 1023) { // TODO
      for (k=0; k<dg; ++k) {
        num[k] += input[k];
        if (num[k] > 9) {
          num[k] %= 10;
          ++num[k+1];
        }
      }
      // counting
      k = num.size() - 1;
      while (num[k] == 0) --k;
      for (k; k>=0; --k) {
        //cout << num[k];
        state |= 1 << num[k];
      }
      //cout << "    " << state << endl;
      //counter++;
    }

    // output
    cout << "Case #" << x << ": ";
    k = num.size() - 1;
    while (num[k] == 0) --k;
    for (k; k>=0; --k) cout << num[k];
    cout << endl;
  }
  return 0;
}
