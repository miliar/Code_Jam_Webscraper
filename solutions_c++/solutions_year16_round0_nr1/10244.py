#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main () {
  int tCases;
  long n;
  int c = 1;
  long mod;
  long result;
  long test;
  long i;
  cin>>tCases;
  while (c <= tCases) {
    cin>>n;
    if (n == 0) {
      cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
    } else {
      int arr [] = {0,1,2,3,4,5,6,7,8,9};
      set<int> digits(arr, arr + 10);
      set<int>::iterator it;
      i = 1;
      while (true) {
        test = i * n;
        result = test;
        while (test != 0) {
          mod = test % 10;
          it = digits.find(mod);
          if (it != digits.end()){
            digits.erase(it);
          }
          test = test / 10;
        }
        if (digits.empty()){
          break;
        }
        i++;
      }
      cout<<"Case #"<<c<<": "<<result<<endl;
    }
    c++;
  }
  return 0;
}
