#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool palindrome(long long n)
{
  vector<int> digits;
  while(n>0)
  {
    digits.push_back(n%10);
    n=n/10;
  }
  bool right=true;
  for(int i=0;i<digits.size();i++)
  {
    if(digits[i]!=digits[digits.size()-1-i]) right=false;
  }
  return right;
}
int main()
{
    int t;
    cin>>t;
    for(int testcase=1;testcase<=t;testcase++)
    {
       long long count=0;
       long long a,b;
       cin>>a>>b;
       for(long long n=ceil(sqrt(a));n<=floor(sqrt(b));n++)
       {
          if(palindrome(n) && palindrome(n*n))
            count++;
       }
       cout<<"Case #"<<testcase<<": "<<count<<endl;
    }
    return 0;
}
