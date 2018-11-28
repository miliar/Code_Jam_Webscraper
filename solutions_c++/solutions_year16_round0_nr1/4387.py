#include <iostream>
#include <vector>
using namespace std;

int findLastNumber(int N) {
  if (N == 0) return -1;
  vector<bool> digitIsSeen(10, false);
  int digitsSeen = 0;
  int M = 0;
  do {
    M += N;
    int P = M;
    while (P > 0) {
      int digit = P % 10;
      if (!digitIsSeen[digit]) {
        digitIsSeen[digit] = true;
        ++digitsSeen;
      }
      P /= 10;
    }    
  } while (digitsSeen < 10);
  return M;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int N; cin >> N;
    int lastNumber = findLastNumber(N);
    cout << "Case #" << (t + 1) << ": ";
    if (lastNumber == -1) {      
      cout << "INSOMNIA" << '\n';
    } else {
      cout << lastNumber << '\n';
    }    
  }  
  cout << flush;
  return 0;
}
