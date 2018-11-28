#include <iostream>
#include <cmath>

using namespace std;

size_t numDigits(size_t num)
{
  int digits = 0;
  
  while(num != 0)
  {
    num /= 10;
    ++digits;
  }
  
  return digits;
}

bool isPalindrome(size_t n)
{
  size_t norig = n;
  
  size_t digits = numDigits(n);
  
  size_t newnum = 0;
  size_t k = pow(10,digits-1);
  
  for(int i=0; i < digits; ++i)
  {
    newnum += k * (n % 10);
    n /= 10;
    k /= 10;
  }
  
  return (newnum == norig);
}

int main()
{
  size_t T;
  cin >> T;
  
  for(int i=0; i < T; ++i)
  {
    size_t A,B;
    cin >> A;
    cin >> B;
    
    size_t a = ceil(sqrt(A));
    
    size_t squared;
    size_t fairandsquare = 0;
    
    do
    {
      squared = a*a;
      
      if(isPalindrome(a) && squared <= B && isPalindrome(squared))
      {
        ++fairandsquare;
      }
      
      ++a;
      
    } while(squared <= B);
    
    cout << "Case #" << i+1 << ": " << fairandsquare << endl;
  }
  
  return 0;
}
