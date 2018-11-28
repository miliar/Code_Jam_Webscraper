#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <stdio.h>      
#include <math.h>       

using namespace std;

typedef map<string,int> Dirs;

long long toBase(unsigned int inNum, int base, int bits)
{
	long long collector=0;
	for (int i=1;i<=bits;i++)
	{
		int bit=inNum>>(bits-i)&0x1;
		collector=collector*base+bit;
	}
	return collector;
}

long long getDivisor(unsigned long long number) 
{
    if (number <= 3 && number > 1) 
        return -1;            // as 2 and 3 are prime
    else if (number%2==0)
		return 2;
	else if (number%3==0) 
        return 3;     // check if number is divisible by 2 or 3
    else 
	{
        unsigned long long i;
        for (i=5; i*i<=number; i+=6) 
		{
            if (number % i == 0)
				return i;
			else if (number%(i + 2) == 0) 
                return i+2;
        }
        return -1; 
    }
}

int main(int argc, char* argv[])
{
  int iCases=0;
  char buffer[50];

  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  cout<< "Case #" << 1 << ":" << endl;

  for (int i=1;i<=iCases;i++)
  {
    int N,J;
    cin >> N >> J;

	int bits=N;
	long long divisors[11];
	bool goodTest=true;
	int foundCases=0;

	int maxCnt=(int)(pow((double)2,(bits-2)));

	for (int i=0;i<maxCnt;i++)
	{
		if (foundCases>=J)
			break;

		memset(divisors,0,sizeof(divisors));

		goodTest=true;

        int testCase=(1<<(bits-1))+(i<<1)+(1);
		//cout << testCase << endl;

	    divisors[2]=getDivisor(testCase);

	    if (divisors[2]!=-1)
	    {
	      for (int i=3;i<=10;i++)
	      {
            long long res=toBase(testCase,i,bits);
	        divisors[i]=getDivisor(res);
		    if (divisors[i]==(-1))
		    {
			  goodTest=false;
			  break;
		    }
	      }
	    }
	    else
	    {
		  goodTest=false;
	    }

		if (goodTest) // (goodTest)
		{
			foundCases++;
            
	        itoa (testCase,buffer,2);

			cout<< buffer;

	        for (int i=2;i<11;i++)
	        {
		      cout<< " " << divisors[i];
	        }

	        cout << endl;
        }
	}
  }
  return 0;
}
