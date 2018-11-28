#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;


//! Counting sheep
int flippingPancakes(
  const string i_pile) {

  //! Previous pancake
  int previous = i_pile[0] == '+';

  //! Special case
  if (i_pile.size() == 1) {
    return 1 - previous;
  }

  //! Number of flips
  int nbFlips = 0;

  //! Loop over the pile of remaining pancakes
  for (size_t n = 1; n < i_pile.size(); n++) {

    //! Look of the current pancakes
    const int current = i_pile[n] == '+';

    //! If equal to the current pancake do nothing
    if (current == previous) {
      continue;
    }
    else {

      //! Flip the previous pile of pancakes
      nbFlips++;
      previous = 1 - previous;
    }
  }

  return nbFlips + 1 - previous;
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
    cout << "Case #" << k << ": " << flippingPancakes(s) << endl;
  }

  return 0;
}
