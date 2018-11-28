#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>


using namespace std;

string fractiles(
  const int K,
  const int C,
  const int S) {

  string res = "";
  for (size_t k = 0; k < K; k++) {
    stringstream ss;
    ss << (k + 1);
    res += " " + ss.str();
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
    int K, C, S;
    cin >> K >> C >> S;

    //! Save the result
    cout << "Case #" << k << ":" << fractiles(K, C, S) << endl;
  }

  return 0;
}
