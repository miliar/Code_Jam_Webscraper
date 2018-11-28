#include <iostream>
#include <sstream>
#include <bitset>

using namespace std;

int main() {

  int T;
  cin >> T;

  for (int t = 0; t < T; t++)
  {
    bitset<10> seen;
    unsigned long long N;
    unsigned long long current = 0;
    cin >> N;

    if (N == 0) {
      cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
      continue;;
    }

    for (int i = 0; i < 1000000; i++)
    {
      current += N;
      unsigned long long rem = current;
      
      while (rem > 0) {
        //cout << "Rem: " << rem << endl;
        //cout << "Digit: " << rem % 10 << endl;

        seen.set(rem % 10);
        rem /= 10;
      }
      //cout << "Current: " << current << ", " << seen.to_string() << endl;

      if (seen.all()) {
        cout << "Case #" << t+1 << ": " << current << endl;
        break;
      }

      if (i == 1000000 - 1) {
        cout << "FAIL" << endl;
      }
    }

  }

  return 0;
}