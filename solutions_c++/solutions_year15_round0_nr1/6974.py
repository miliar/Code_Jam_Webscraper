#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int main (void) {
  long long T;
  cin >> T;

  for(long long i = 0; i < T; i++) {
    long long smax;
    cin >> smax;

    string digits;
    cin >> digits;

    long long S = 0;
    long long freq = 0;
    long long res = 0;

    for(long long j = 0; j < digits.length(); j++) {
      freq = digits[j] - '0';

      if(S < j && freq != 0) {
        res += (j-S);
        S += (j-S);
      }

      S += freq;
    }

    cout << "Case #" << (i+1) << ": " << res << endl;
  }  
  return 0;
}
