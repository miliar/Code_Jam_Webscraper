#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>

using namespace std;

bool check(long number) {
  stringstream ss;
  
  ss << number;
  
  string numberString = ss.str();
  
  bool isPalindrom = true;
  
  int left = 0;
  int right = numberString.length() - 1;
  
  int center = numberString.length() / 2;
  
  while (right >= center && left <= center) {
   
    if (numberString[left] != numberString[right]) {
      isPalindrom = false;
      break;
    }
  
    left++;
    right--;  
  }
  
  return isPalindrom;
}

int main(int argc, char* argv[])
{
  int t;
  
  cin >> t;
  
  long a, b;
   
  int result;
  
  //precalculations
  
  vector<long> numbers;
  
  long y;
  
  for (long x = 1; x <= sqrt(100000000000000); x++) {    
    if (check(x)) {
      y = x * x;
      
      if (check(y)) {
        numbers.push_back(y);
      }
    }
  }
  
  
  for (int i = 0; i < t; i++) {
    cin >> a >> b;
   
    result = 0;
     
    int index = 0;
    
    while (numbers[index] < a) {
      index++;
    }
    
    while (numbers[index] <= b && index < numbers.size()) {
      index++;
      result++;
    }
    
    cout << "Case #" << i + 1 << ": ";
      
    cout << result << endl;
  }
  
  return 0;
}
