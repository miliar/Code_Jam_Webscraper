#include <iostream>
#include <string>
#include <cmath>
#include <sstream>

using namespace std;

long long unsigned all[1000000];
int total_found = 0;

bool isPalindrome(long long unsigned number) {
  stringstream ss;
  ss << number;
  string str = ss.str();  
  for(unsigned i = 0; i < str.length() / 2; ++i) {
    if(str[i] != str[str.length()-1-i]) {
      return false;
    }
  }
  return true;
}

int solve(long long unsigned A, long long unsigned B) {
  int count = 0;
  long long unsigned start = ceil(sqrt(A));
  long long unsigned end = floor(sqrt(B));
  for(long long unsigned i = start; i <= end; ++i) {
    if(isPalindrome(i) && isPalindrome(pow(i,2))) {
      all[total_found] = pow(i,2);
      count++;
      total_found ++;
      clog << "found: " << i << endl;
    }
  }
  return count;
}

int main() {
  solve(1,1000000000000000);
  
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    long long unsigned A;
    long long unsigned B;
    int res = 0;    
    cin >> A;
    cin >> B;
    for(int j = 0; j < total_found; ++j) {
      if(all[j] >= A && all[j] <= B) res++;
    }
    cout << "Case #" << i << ": " << res << endl;
  }
  
  return 0;
}
