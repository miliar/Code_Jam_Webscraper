#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
long countSheep(long n);

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    cout << "Case #" << i << ": ";
    if (n==0) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << countSheep(n) << endl;
    }
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}

long countSheep(long n) {
  int digitCount[10] ={0,0,0,0,0,0,0,0,0,0};
  long i = 1;
  string val = "";
  int currDigit = 0;
  
  while((find(digitCount, digitCount+10, 0)!= digitCount+10)){
    val = to_string(i*n);
    for(long j=0;j<val.size();j++){
      currDigit = val[j] - '0';
      digitCount[currDigit]++;
    }
    i++;

  }
  
  return stol(val);
}