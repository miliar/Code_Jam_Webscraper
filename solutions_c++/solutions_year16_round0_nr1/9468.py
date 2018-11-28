#include <iostream>
#include <set>
using namespace std;

bool seenAll(set<int>& digits, long i, long N) {
  //cout << i << "N=" << i*N << "\n";
  long iN = i*N;
  while(iN > 0) {
    if(digits.insert(iN%10).second) {
      //cout << " seen " << (iN%10) << "\n";
    }
    iN /= 10;
  }
  return digits.size() == 10;
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for(int ca=0; ca<T; ++ca) {
    long N;
    cin >> N;

    bool impossible = N == 0;
    set<int> digits;
    long i = 1;
    while(!impossible && !seenAll(digits, i, N)) {
      i++;
    }

    if(impossible) {
      cout << "Case #" << (ca+1) << ": INSOMNIA\n";
    } else {
      cout << "Case #" << (ca+1) << ": " << i*N << "\n";
    }
  }

  return 0;
}
