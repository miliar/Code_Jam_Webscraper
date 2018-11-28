#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;


//! Counting sheep
string countingSheep(
  const int i_N) {

  //! Special case
  if (i_N == 0) {
    return string("INSOMNIA");
  }

  //! Initialization of the array of integer seen
  int N = i_N;
  vector<int> integer(10, 0);

  //! Otherwise
  bool stop = false;
  while (!stop) {

    //! Transform int to string
    stringstream ss;
    ss << N;
    string s = ss.str();

    //! Look the new number obtained
    for (size_t n = 0; n < s.size(); n++) {
      int k = int(s[n]) - 48;

      //! Update the array
      integer[k]++;
    }

    //! Stop when all the integer has been seen
    stop = true;
    for (size_t n = 0; n < integer.size(); n++) {
      if (integer[n] == 0) {
        stop = false;
        N += i_N;
        break;
      }
    }
  }

  //! Transform the result int to string
  stringstream ss;
  ss << N;
  return ss.str();
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
    int n;
    cin >> n;

    //! Save the result
    cout << "Case #" << k << ": " << countingSheep(n) << endl;
  }

  return 0;
}
