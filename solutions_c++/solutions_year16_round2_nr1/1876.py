#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

void gettingDigits(
  const string s,
  std::vector<int>& numbers) {

  vector<int> letters(26, 0);

  for (size_t k = 0; k < s.size(); k++) {
    letters[int(s[k]) - 65]++;
  }

  //! Zero
  if (letters[25] > 0) {
    for (int k = 0; k < letters[25]; k++) {
      numbers.push_back(0);
      letters[4]--;
      letters[17]--;
      letters[14]--;
    }
    letters[25] = 0;
  }

  //! Two
  if (letters[22] > 0) {
    for (int k = 0; k < letters[22]; k++) {
      numbers.push_back(2);
      letters[19]--;
      letters[14]--;
    }
    letters[22] = 0;
  }

  //! Four
  if (letters[20] > 0) {
    for (int k = 0; k < letters[20]; k++) {
      numbers.push_back(4);
      letters[5]--;
      letters[14]--;
      letters[17]--;
    }
    letters[20] = 0;
  }

  //! Six
  if (letters[23] > 0) {
    for (int k = 0; k < letters[23]; k++) {
      numbers.push_back(6);
      letters[18]--;
      letters[8]--;
    }
    letters[23] = 0;
  }

  //! Eight
  if (letters[6] > 0) {
    for (int k = 0; k < letters[6]; k++) {
      numbers.push_back(8);
      letters[4]--;
      letters[8]--;
      letters[7]--;
      letters[19]--;
    }
    letters[6] = 0;
  }

  //! Three
  if (letters[7] > 0) {
    for (int k = 0; k < letters[7]; k++) {
      numbers.push_back(3);
      letters[19]--;
      letters[17]--;
      letters[4]--;
      letters[4]--;
    }
    letters[7] = 0;
  }

  //! Five
  if (letters[5] > 0) {
    for (int k = 0; k < letters[5]; k++) {
      numbers.push_back(5);
      letters[8]--;
      letters[21]--;
      letters[4]--;
    }
    letters[5] = 0;
  }

  //! Seven
  if (letters[21] > 0) {
    for (int k = 0; k < letters[21]; k++) {
      numbers.push_back(7);
      letters[18]--;
      letters[4]--;
      letters[4]--;
      letters[13]--;
    }
    letters[21] = 0;
  }

  //! One
  if (letters[14] > 0) {
    for (int k = 0; k < letters[14]; k++) {
      numbers.push_back(1);
      letters[13]--;
      letters[4]--;
    }
    letters[14] = 0;
  }

  //! Nine
  if (letters[4] > 0) {
    for (int k = 0; k < letters[4]; k++) {
      numbers.push_back(9);
      letters[13]--;
      letters[8]--;
      letters[13]--;
    }
    letters[4] = 0;
  }

  sort(numbers.begin(), numbers.end());
}


//! Main function
int main()
{
  //! Read the first line of the file to know the total of test
  int T;
  cin >> T;

  //! Print the lines after that
  for (int k = 1; k <= T; k++) {

    //! Read the value
    string s;
    cin >> s;

    //! Save the result
    std::vector<int> numbers;
    gettingDigits(s, numbers);
    cout << "Case #" << k << ": ";
    for (size_t k = 0; k < numbers.size(); k++) {
      cout << numbers[k];
    }
    cout << endl;
  }

  return 0;
}
