

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main()
{
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');//for removing trailing spaces to endof line
  for(int i = 1; i <= t; ++i) {
    int K,C,S;
    cin >> K >> C >> S;
    if(K == S){//Small problem
      //take into account the first k (=s) tiles are all G (if first was a G) or a repetition of the original sequence (if first was L)
      cout << "Case #" << i << ":";
      for(int i = 1; i <= S; ++i)
        cout << " " << i;
      cout << endl;
    }
    else{
      cout << "Case #" << i << ":" << "not implemented" <<endl;
    }
  }

  return 0;
}

