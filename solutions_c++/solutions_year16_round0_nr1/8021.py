#include <iostream>
#include <vector>

using namespace std;

void count_digits(long num, vector<bool> &result) {
  for(;num > 0; num/= 10) {
    long digit = num % 10;
    result[digit] = true;
  }
}

int main(void) {
  int T;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    long N;
    cin >> N;
    vector<bool> asleep(10, false);
    bool allseen = false;
    long lastnumber = -1;
    for(long i = 1; i <= 100; ++i) {
      count_digits(i * N, asleep);
      allseen = true;
      for(int ii = 0; ii < 10; ++ii) {
        if(!asleep[ii]) {
          allseen = false;
        }
      }
      if(allseen) {
        lastnumber = i * N;
        break;
      }
    }
    cout << "Case #" << t << ": ";
    if(lastnumber == -1) {
      cout << "INSOMNIA";
    } else {
      cout << lastnumber;
    }
    cout << endl;
  }
  return 0;
}
