#include <iostream>
#include <cstdio>
using namespace std;
bool isPalindrome(long long n)
{
  string str = "";
  while(n > 0){
    str += (n % 10) + '0';
    n /= 10;
  }
  int i=0, j = str.length()-1;
  bool bOK = true;
  while(i<j)
    if(str[i++] != str[j--]) return false;
  return true;
}
int main()
{
  int T;
  cin >> T;
  for(int ca = 1; ca<=T; ca++){
    long long min,max;
    cin >> min >> max;
    long long i=1;
    while(i * i < min) i++;
    long long count = 0;
    for(; i * i <= max; i++)
      if(isPalindrome(i) && isPalindrome(i * i)) count++;
    printf("Case #%d: %d\n", ca, count);
  }
  return 0;
}
