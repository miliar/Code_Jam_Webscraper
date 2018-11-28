#include <iostream>
#include <string>
#include <vector> 
#include <sstream>
#include <math.h>

using namespace std;

bool isPalindrome(const string& s) {
  for (int i=0;i<s.length()/2;i++)
    if (s.substr(i, 1) != s.substr(s.length()-i-1, 1))
      return false;

  return true;
}

string addOne(string s) {
  int i;

  for (i=s.length()-1; i>=0; i--) {
    char thisVal = s.substr(i, 1).c_str()[0] + 1;

    if (thisVal == ':') {
      // This entry becomes zero, proceed with adding one to the next.
      s.replace(i, 1, 1, '0');
    } else {
      s.replace(i, 1, 1, thisVal);
      break;
    }
  }

  if (i == -1) {
    s = "1" + s;
  }

  return s;
}

string nextPalindrome(const string& s) {
  // Inclusive on middle one.
  string firsthalf = s.substr(0, (s.length() + 1) / 2);
  string secondhalf;

  bool odd = (s.length() % 2 == 1) ? true : false;

  // First determine if the palindrome of the first half is larger than the second half.  If so, 
  // I need to return THAT palindrome
  string result = firsthalf;

  if (odd) {
    for (int i=firsthalf.length()-2; i>=0; i--) {
      result = result + firsthalf.substr(i, 1);
    }
  } else {
    for (int i=firsthalf.length()-1; i>=0; i--) {
      result =  result + firsthalf.substr(i, 1);
    }
  }

  string newfirsthalf;

  if (result > s) {
    return result;
  } else {
    // Increment the first half. 
    newfirsthalf = addOne(firsthalf);

    // If we need to increase length by one, need to switch  
    if (newfirsthalf.length() == firsthalf.length() + 1) {
      if (odd) {
        newfirsthalf = newfirsthalf.substr(0, newfirsthalf.length()-1);
        odd = !odd;
      } else {
        odd = !odd;
      }
    }
  }

  firsthalf = newfirsthalf;

  // If odd, mirror it except the last char.
  if (odd) {
    secondhalf = "";

    for (int i=0; i<firsthalf.length()-1; i++) {
      secondhalf = firsthalf.substr(i, 1) + secondhalf;
    }

    return firsthalf + secondhalf;
  } else {
    // Otherwise just mirror it.
    secondhalf = "";

    for (int i=0; i<firsthalf.length(); i++) {
      secondhalf = firsthalf.substr(i, 1) + secondhalf;
    }

    return firsthalf + secondhalf;
  }
}

string square(string s) {
  long long val;
  long long result;

  istringstream ( s ) >> val;

  result = val * val;

  ostringstream convert;   

  convert << result;   

  return convert.str();
}

string sqrtRoundDown(string s) {
  long long val;
  long long result;

  istringstream ( s ) >> val;

  result = floor(sqrt(val));  

  ostringstream convert;   

  convert << result;      

  return convert.str();
}

string sqrtRoundUp(string s) {
  long long val;
  long long result;

  istringstream ( s ) >> val;

  result = ceil(sqrt(val));

  ostringstream convert;   

  convert << result;      

  return convert.str();
}

int main() {
  int cases;

  cin >> cases;
  for (int i=0; i<cases; i++) {
    string a;
    string b;

    cin >> a >> b;

    // Find the minimum and maximum that I have to try.
    string start = sqrtRoundUp(a);
    string end = sqrtRoundDown(b);

    string current = start;

    int cnt = 0;
    while ((current.length() < end.length()) || (current <= end)) {
      if (isPalindrome(square(current)))
        cnt++;

      current = nextPalindrome(current);
    }


    cout << "Case #" << i + 1 << ": " << cnt << "\n";
  }

  return 0;
}
