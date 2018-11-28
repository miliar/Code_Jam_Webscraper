#include <iostream>
#include <string>
using namespace std;

int sum(int *digits) {
  int sum = 0;
  for (int i = 0; i<10; i++){
    sum+=digits[i];
  }
  return sum;
}

int compute(int number) {
  int digits[10];
  for (int i = 0; i<10; i++) {
    digits[i]=0;
  }
  
  int digit;
  int actual;
  int i = 0;
  while (sum(digits)<10) {
    if (i >100) {
      return 0;
    }
    i++;
    actual = i*number;
    while (actual > 0) {
      digit = actual % 10;
      digits[digit] = 1;
      actual = (int) (actual / 10);
    }
  }
  return i*number;
}

int main(int argc, char **argv) {
  
    int t;
    std::cin >> t;
    
    int number;
    int result;
    
    for (int i = 1; i <= t; i++) {
      cin >> number;
      cout << "Case #" << i << ": ";
      result = compute(number);
      if (result == 0) {
	cout << "INSOMNIA" << endl;
      } else {
	cout << result << endl;
      }
    }
    
    return 0;
}
