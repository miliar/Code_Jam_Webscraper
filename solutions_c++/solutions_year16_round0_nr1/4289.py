#include <iostream>
#include <set>


using namespace std;

int main() {
  int T;
  cin >> T;

  for(int j = 1; j <= T; j++) {
    int N;
    cin >> N;
    if(N == 0) {
      cout << "Case #" << j << ": " << "INSOMNIA" << endl;
    } else {
      set<int> seen_digits;
      for(int i = 1; ; i++) {
        int current = N * i;
        while(current > 0) {
          seen_digits.insert(current % 10);
          current /= 10;
        }
        if(seen_digits.size() == 10) {
          cout << "Case #" << j << ": " << N*i << endl;
          break;
        }
      }
    }

  }
}
