#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int tester(int val)
{
  bool nums[10] = {false};
  int count = 1;
  int newVal = val;
  while(true)
  {
    newVal = val*count;
    // Add digits to bool array
    int n = newVal;
    do {
      int digit = n % 10;
      nums[digit] = true;
      n /= 10;
    } while (n > 0);
    // Check if bool array is all true
    int checker = 0;
    for(int i = 0; i <= 9; ++i)
    {
      if(nums[i])
      {
        checker++;
      }
    }
    if(checker == 10)
    {
      return(newVal);
    }
    count = count + 1;
  }
  return 0;
}

int main() {
  int t, n, last;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    if(n == 0)
    {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
    else
    {
      last = tester(n);
      cout << "Case #" << i << ": " << last << endl;
    } 
  }
  return 0;
}
