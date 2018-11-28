#include <iostream>
#include <bitset>
using namespace std;

bitset<10> digits;
void check(long long N)
{
  long long i=1;
  while(N!=0)
    {
      int a=N%10;
      digits.set(a);
      N/=10;
    }
}

int main()
{
  int T; cin >> T;
  for (int i=1; i<=T; i++)
    {
      long long origN; cin >> origN;
      long long N=0;
      cout << "Case #" << i << ": ";
      digits.reset();
      if (origN==0)
	cout << "INSOMNIA" << endl;
      else
	{
	  while(!digits.all())
	    {
	      N+=origN;
	      check(N);
	    }
	  cout << N << endl;
	}   
    }
}
