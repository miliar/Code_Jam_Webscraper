/** Counting Sheep
 * Author: Don Vo
 * Solution to Google Jam's Problem A
 * Google Coding Jam 2016
 * Problem A: Counting Sheep
 */
#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int const NUM_DIGITS = 10;

int main(void) {

  // Declare a place to fill digits and decide on # of cases
  vector<bool> digits;
  digits.resize(10, false);
  int numCases;
  cin >> numCases;

  int current;
  int copy;
  int digit;
  int numDigits = 0;
  int lastNum = 0;

  for (int i = 0; i < numCases; i++) {

    // Clear elements in the vector
    for (int j = 0; j < NUM_DIGITS; j++) {
      digits[j] = false;
    }
    numDigits = 0;
    lastNum = 0;

    // Make a check in case the program runs forever
    cin >> current;
    cout << "Case #" << (1 + i) << ": ";
    if (current == 0) {
      cout << "INSOMNIA\n";
      continue;
    }

    // Loop until we check each digit in current integer
    while (numDigits < NUM_DIGITS) {
      lastNum += current;
      copy = lastNum;
      while (copy > 0) {
	digit = copy % NUM_DIGITS;
	copy /= NUM_DIGITS;
	if (digits[digit] == false) {
	  digits[digit] = true;
	  numDigits++;
	}
      }
    }
    cout << lastNum << "\n";
  }


}
