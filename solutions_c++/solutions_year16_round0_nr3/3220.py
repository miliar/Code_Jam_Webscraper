#include <iostream>
#include <bitset>

using namespace std;

long long int toBase(int i, int radix) {
  long long int ret = 0;
  long long int place = 1;
  while(i > 0) {
    if(i & 1 == 1) {
      ret += place;
    }
    i = i >> 1;
    place *= radix;
  }
  return ret;
}

long long int div(long long int i) {
  for(long long int j = 2; j * j <= i; j++) {
    if(i % j == 0)
      return j;
  }
  return -1;
}

int main() {
  int loops, n, j;
  cin >> loops;
  for(int loop = 1; loop <= loops; loop++) {
    cin >> n >> j;

    int START = 1 + (1 << (n - 1));
    int END = 1 << n;

    // cout << (toBase(START, 10)) << endl;
    // cout << (toBase(END, 10)) << endl;

    cout << "Case #" << loop << ":" << endl;

    long long int divs[11];
    int found = 0;
    for(int i = START; i < END && found < j; i+=2) {
      bool isJam = true;
      // cout << bitset<16>(i) << endl;
      for(int radix = 2; radix <= 10; radix++) {
        int divisor = div(toBase(i, radix));
        // cout << toBase(i, radix) << " ";
        if(divisor == -1) {
          isJam = false;
          break;
        }
        divs[radix] = divisor;
      }
      // cout << endl;
      if(isJam) {
        found++;
        cout << bitset<16>(i);
        for(int radix = 2; radix <= 10; radix++) {
          cout << " " << divs[radix];
        }
        cout << endl;
      }
    }


  }
}