#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>

using namespace std;

typedef map<string,int> Dirs;

int main(int argc, char* argv[])
{
  int iCases=0;
 
  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int i=1;i<=iCases;i++)
  {
    unsigned long long N=0;

	unsigned long long lastVal=0;
    cin >> N;
    unsigned int iMaxTries=450000;
	int seenDigits=0;
	int digits[10];
	memset(digits,0,sizeof(digits));

    for (unsigned int j=1;j<iMaxTries;j++)
    {
      unsigned long long val=N*(unsigned long long)j;
	  string valStr=to_string(val);
	  for (unsigned int k=0;k<valStr.length();k++)
	  {
		  int pos=(*(valStr.c_str()+k))-'0';
		  int dcnt=digits[pos];
		  if (dcnt==0)
  		    seenDigits++;

		  digits[pos]=1;
	  }
	  if (seenDigits>=10)
	  {
		  lastVal=val;
		  break;
	  }
    }

	cout<< "Case #" << i << ": ";

	if (seenDigits>=10)
	{
	    cout<<  lastVal << endl;
	}
	else
	{
		cout<< "INSOMNIA" << endl;
	}
  }
  return 0;
}
