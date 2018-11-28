#include<iostream>
#include<set>
using namespace std;

int main()
{
  int t;
  cin>>t;
  for(int test =0; test < t; test++)
    {
      long long n;
      cin>>n;
      if(n==0){
        printf("Case #%d: INSOMNIA\n", test + 1);
        continue;
      }
      set<int> digits;
      int mul = 1;
      while(digits.size() < 10)
        {
          long long num = mul * n;
          while(num)
            {
              int dig = num % 10;
              digits.insert(dig);
              num /= 10;
            }
          mul++;
        }
      printf("Case #%d: %lld\n", test + 1, n * (mul - 1));
    }
}
