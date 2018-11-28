#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <sstream>
#include <climits>
#include <cmath>
#include <string>

using namespace std;


bool is_palindrome(string str){
  if(str.length() == 1 || str.length() == 0) return true;
  
  return (str[0] == str[str.length()-1]
	  && is_palindrome(str.substr(1, str.length()-2)));
}

bool square_perfect(int number){
  double sqr = sqrt((double)number);
  return ((int)sqr*(int)sqr == number);
}

bool is_square_palindrome(int number){
  int square = sqrt(number);
  stringstream ss;
  ss.str("");
  ss << square;
  string number_squared = ss.str();
  return is_palindrome(number_squared);
}

int main(){
  int T;
  cin >> T;
  int min, max;
  stringstream ss;
  string num_as_string;
  int counter;
  for(int i=0; i<T; ++i){
    cin >> min >> max;
    counter = 0;
    for(int j=min; j<=max; ++j){
      ss.str("");
      ss << j;
      num_as_string = ss.str();
      if(is_palindrome(num_as_string) && square_perfect(j) && is_square_palindrome(j)){
	counter++;
      }
    }
    cout << "Case #" << i+1 << ": " << counter << endl;
  }
  return 1;
}
