#include<iostream>
#include<math.h>
using namespace std;

bool checkPallindrome(long long val)
{
  long long number = val;
  long long revnumber = 0;
  while(number!=0)
  {
    revnumber = revnumber*10 + number%10;
    number = number/10;
  }
  if(revnumber == val)
    return true;
  else
    return false;
}

int main()
{
  int testcases;
  cin>>testcases;
  for(int t =0;t< testcases;t++)
  {
    long long min,max;
    cin>>min>>max;
    long double minsqrt = sqrt(double(min));
    long double maxsqrt = sqrt(double(max));
    long long minlimit = ceil(minsqrt);
    long long maxlimit = floor(maxsqrt);
    long long count = 0;
    for(long long int i = minlimit;i<=maxlimit;i++)
    {
	 bool childPallindrome = false;
	 bool parentPallindrome = false;
	 childPallindrome = checkPallindrome(i);
	 if(childPallindrome)
	 {
	   parentPallindrome = checkPallindrome(i*i);
	   if(parentPallindrome)
	   {
		count++;
		//cout<<i<<"\n";
	   }
	 }
    }
        cout<<"Case #"<<t+1<<": "<<count<<"\n";
  }
  /*long long number = pow(double(10),double(13));
  cout<<number<<"\n";
  long long sqrtnumber = sqrt(double(number-1));
  cout<<sqrtnumber;*/

}