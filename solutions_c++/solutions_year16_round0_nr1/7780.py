#include<iostream>
#include<map>
using namespace std;

void fillDigits(int num, map<int, int> &digit) {
  while (num != 0) {
    digit[num%10] = 1;
    num /= 10; 
  }
}

int solve(int n) {
  map<int, int> numbers, digits;
  int num = n;
  while (digits.size() < 10) {
    fillDigits(num, digits);
    if (numbers[num] != 0) {
      return 0;
    }   
    numbers[num] = 1;
    num = num + n;
  }
  return num - n;
}

int main() {
  int t;
  cin >> t;
  for (int i=1; i<=t; i++) {
    int n;
    cin >> n;
    cout << "Case #" << i << ": ";
    int res = solve(n);
    if (res == 0) {
      cout << "INSOMNIA";
    } else {
      cout << res;
    }   
    cout << endl;
  }
}

