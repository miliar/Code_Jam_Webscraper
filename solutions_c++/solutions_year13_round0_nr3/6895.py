#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include<cmath>

using namespace std;

bool isPalindrome(int num) {
    int rev = 0;
    int n = num;

    while(n != 0) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }

    if(rev == num) return true;
    else return false;
}

int main()
{

  ifstream is;
  std::ofstream os("output.txt");


  is.open("C-small-attempt0.in");

  int count, start, end, ans = 0; 

  is >> count;

  for(int i = 0; i < count; i++) {
      is >> start >> end;

      for(int j = start; j <= end; j++) {
          if(isPalindrome(j) && isPalindrome(sqrt(j))) {
              if((int)sqrt(j)*(int)sqrt(j) == j) {
                 
                  ans++;
              }
          }
      }

      os << "Case #" << i + 1 << ": " << ans << endl;
      ans = 0;

  }

  
  os.close();
  is.close();
  cin.get();
  return 0;
}