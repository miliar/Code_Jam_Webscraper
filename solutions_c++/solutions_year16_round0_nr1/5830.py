#include <iostream>

using namespace std;

bool* digitsInNumber(int n) {
  bool found[10] = {false,false,false,false,false,false,false,false,false,false};
  int founds = 0;
  while (n > 0 && founds != 10) {
    int currentDigit = n % 10;
    if (!found[currentDigit]) {
      found[currentDigit] = true;
      founds++;
    }
    n = n / 10;
  }
  return found;
}

int main() {
  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {

    bool found[10] = {false,false,false,false,false,false,false,false,false,false};
    int founds = 0;
    int N;
    int sol = 0;

    cin>>N;

    if (N == 0) {
      cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
    } else {

      int k = 1;
      while(founds != 10) {
        founds = 0;
        bool* currentNumber = digitsInNumber(N * k);
        for (int j = 0; j < 10; j++) {
          found[j] = found[j] || currentNumber[j];
          if (found[j]) founds++;
        }
        k++;
      }
      k--;
      cout<<"Case #"<<(i+1)<<": "<<(N * k)<<endl;
    }
  }

  return 0;
}
