#include <stdio.h>
#include <vector>
#include <math.h>

using namespace std;

bool is_palindrome(long long i)
{
  long long temp = i;
  long long reverse = 0;

  while(temp)
  {
    reverse = reverse*10 + temp%10;
    temp = temp/10;
  }

  if(reverse == i)
    return true;
  else
    return false;
}

int main()
{
  vector<long long> numbers;
  long long T, A, B, temp, count;
  scanf("%lld", &T);

  for(long long i = 1; i <= pow(10,7); i++)
  {
    if(is_palindrome(i))
    {
      if(is_palindrome(i*i))
      {
        //printf("%lld\n", (long long)(i*i));
        numbers.push_back(i*i);
      }
    }
  }
 
  for(int tc = 1; tc <= T; tc++)
  {
    scanf("%lld %lld", &A, &B);
    
    count = 0;
    for(int i = 0; i < numbers.size(); i++)
    {
      if(A <= numbers[i] && B>= numbers[i])
        count++;
    }
    
    printf("Case #%d: %lld\n", tc, count);

  }
  
}
