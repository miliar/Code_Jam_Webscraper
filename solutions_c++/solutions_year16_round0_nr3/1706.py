#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <stack>
#include <iomanip>
using namespace std;

long long isPrime(long long base2)
{
  //cout << base2 << endl;
  while(base2%3!=0)
    base2+=2;
  //cout << base2 << endl;
  return base2;
}

string binary(long long number)
{
  int len;
  char ch;
  string out;
  
  while(number>0)
    {
      out+=static_cast<char>(number%2)+'0';
      number/=2;
    }
  
  len=out.length();
  
  for(int i=0;i<=len;i++)
    {
      ch=out.at(i);
      out.at(i)=out.at(--len);
      out.at(len)=ch;
    }
  
  return out;
}

bool eleven(string s)
{
  int count=0;
  for(int i=0;i<s.length();i++)
    {
      if (s.at(i)=='1')
	{
	  if (i%2==0)
	    count++;
	  else
	    count--;
	}
    }
  return count;
    
}

long long arrayBase2[32]={2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
			  2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,
			  2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824,
			  2147483648, 4294967296};

int main()
{
  //int list[6]={3,5,7,13,21,31};
  int T; cin >> T;
  for (int i=1;i<=T;i++)
    {
      int N;
      int J;
      cin >> N >> J;
      long long base2=arrayBase2[N-2]+1;
      long long upper=arrayBase2[N-1]-1;
      cout << "Case #" << i << ":" << endl;
      base2=isPrime(base2);
      while(J&&base2<=upper)
	{
	  string s = binary(base2);
	  if (!eleven(s))
	    {
	      cout << binary(base2) <<" 3 4 5 6 7 8 9 10 11" << endl;
	      J--;
	    }
	  base2+=6;
	}
    }
}
