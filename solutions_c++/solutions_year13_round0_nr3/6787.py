#include<iostream>
#include<Math.h>
#include<cstring>
#include<sstream>
#include<cctype>
#include<fstream>
using namespace std;
string convertInt(long long number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

bool ispal(string s)
{
int len = s.length();
for (int i=0; i<len/2; i++)

	if(s[i]!= s[len-i-1])return false;
	return true;

}

bool IsSquare(long long n)
{
	if(ispal(convertInt(n)))
	{
		bool issquare;
		float sq= sqrt(n);
		int sqr= (int )sq;
		float rem = sq - (float)sqr;
		if(rem > 0.00)
		{
			issquare = false;
			return false;
		}
		else
		{
			issquare = true;
			string sqrr =convertInt(sqr);
				if (ispal(sqrr))
				{
					return true;
				}
				else
				{
				return false;
				}

		}
	}
	else
	{
		return false;
	}
}

ifstream fin("filein.txt");
ofstream fout("fileout.txt");
int main()
{
	int N, ct=0;
	long long lim1, lim2;
	fin>> N;
	for(int i= 1; i<= N; i++)
	{
		fout<< "Case #" <<i<<": ";
		fin>> lim1 >> lim2;
		for(long long j= lim1; j<= lim2; j++)
		{
			if(IsSquare(j))
			ct++;
		}
		
		fout<< ct<<  "\n";
		ct=0;
	}

}
