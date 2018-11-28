#include <iostream>
#include <math.h>
using namespace std;

bool isPalindrome (unsigned long int n)
{
 unsigned long int num=n, digit, rev = 0;
  do
    {
      digit = num%10;
      rev = (rev*10) + digit;
      num = num/10;
    }while (num!=0);
  if (n == rev)
    {
      return true;
    }
  else
    {
      return false;
    }
}

void fairAndSquare(unsigned long int A,unsigned long int B)
{
   double refinedIntervalA=sqrt(( double)A),refinedIntervalB=sqrt(( double)B);
   unsigned long int lowA=static_cast<unsigned long int>(ceil(refinedIntervalA));
  unsigned long int lowB=static_cast<unsigned long int>(floor(refinedIntervalB));
  unsigned int nfairAndSquare=0;
  for (unsigned long int i=lowA;i<=lowB;i++)
    {
      if (isPalindrome(i) && isPalindrome(i*i))
	nfairAndSquare++;
    }
  cout<<nfairAndSquare;
}

int main ()
{
  unsigned int tcases;
  cin>>tcases;
  for(unsigned long int i=0;i<tcases;i++)
    {
      unsigned long int A,B;
      cin>>A;
      cin>>B;
      cout<<"Case #"<<i+1<<": ";
      fairAndSquare(A,B);
      cout<<endl;
    }
  return 0;
}
