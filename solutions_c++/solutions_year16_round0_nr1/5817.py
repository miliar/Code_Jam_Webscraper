#include <iostream>
using namespace std;
int main() {
  int t, n; 
  cin >> t;
  
  int expectedSum = 0;
  for (int i = 0; i <= 9; i++) {
      expectedSum += i+1;
  }
  
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    int currentSum = 0;
    bool foundDigits[10];
    std::fill(foundDigits, foundDigits+10, false);
    int currentNumber = 0;
    while (currentSum < expectedSum && n != 0) {
        currentNumber += n;
        int breakingNumber = currentNumber;
        
        do {
            int digit = breakingNumber % 10;
            if (!foundDigits[digit]) {
                foundDigits[digit] = true;
                currentSum += digit + 1;
            }
            breakingNumber /= 10;
        } while (breakingNumber > 0);
    }
    if (currentNumber == 0)
        cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    else
        cout << "Case #" << i << ": " << currentNumber << endl;
  }
  
  return 0;
}
