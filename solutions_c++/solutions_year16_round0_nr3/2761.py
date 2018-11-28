#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <stdio.h>

using namespace std;

//! Given a string, get the new one
void nextString(
  string &s) {

  for (size_t n = s.size() - 2; n > 0; n--) {
    if (s[n] == '0') {
      s[n] = '1';
      return;
    }
    else {
      s[n] = '0';
    }
  }
}


//! Obtain the number in the wanted base
long long int getNumber(
  const string s,
  const long long int base) {

  long long int b = 1;
  long long int number = 0;
  for (int n = s.size() - 1; n >= 0; n--) {
    number += b * (long long int) (s[n] == '1');
    b *= base;
  }

  return number;
}


//! Check if the given number isn't prime, and give it's first divider > 1
long long int isNotPrime(
  const long long int n) {

  //! Special case
  if (n % 2 == 0) {
    return 2;
  }
  else {
    const long long int K = sqrt(n);
    for (long long int k = 3; k <= K; k += 2) {
      if (n % k == 0) {
        return k;
      }
    }
  }
  return 0;
}


//! Counting sheep
string coinJam(
  const int N,
  const int J) {

  int j = 0;
  string res = "";
  string s = "1" + string(N - 2, '0') + "1";
  //cout << "s = " << s << endl;

  //! While J coinJam haven't been found, keep going
  while (j < J) {

    //! Hope it's valid
    bool isValid = true;

    //! Loop over each base
    vector<long long int> divider(9);
    for (int n = 2; n <= 10; n++) {

      //! Get the number in base 10
      const long long int number = getNumber(s, n);

      //! Check if it's prime
      divider[n - 2] = isNotPrime(number);
      isValid = isValid && divider[n - 2] > 0;
      //cout << "n = " << number << ", d = " << divider[n - 2] << endl;
      if (!isValid) {
        break;
      }
    }

    if (isValid) {
      res += s;
      for (int n = 2; n <= 10; n++) {
        stringstream ss;
        ss << divider[n - 2];
        res += " " + ss.str();
      }
      res += "\n";
      j++;
    }

    //! Obtain a new tentative
    nextString(s);
  }

  return res;
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
    int n, j;
    cin >> n >> j;

    //! Save the result
    cout << "Case #" << k << ":\n" << coinJam(n, j) << endl;
  }

  return 0;
}
