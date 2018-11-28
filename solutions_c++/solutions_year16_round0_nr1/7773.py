#include <iostream>
#include <vector>
using namespace std;

int add(int x, vector<bool>& flag) {
  int out = 0;
  while(x > 0) {
    if (!flag[x%10]) {
      flag[x%10] = true;
      ++out;
    }
    x /= 10;
  }
  return out;
}

int count(int N) {
  if (N == 0)
    return -1;
  vector<bool> flag(10, false);
  int c = 10, x = 0;
  while(c != 0) {
    x += N;
    c -= add(x, flag);
  }
  return x;
}

int main() {
  int T, N, out, i;
  cin >> T;
  for(i = 0; i < T; ++i){
    cin >> N;
    out = count(N);
    if (out == -1)
      cout << "Case #" << i+1 << ": INSOMNIA";
    else
      cout << "Case #" << i+1 << ": " << out;
    cout << endl;
  }
  return 0;
}