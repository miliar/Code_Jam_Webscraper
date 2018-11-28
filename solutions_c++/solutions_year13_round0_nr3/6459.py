#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

int getValue(ifstream& infile)
{
	string line;
	getline(infile,line);
	return atoi(line.c_str());
}

bool palindrome(int number)
{
	bool Palind = true;
	string _num = to_string(number);
	int _numlen = _num.length();
	if(_numlen > 1)
	{
		if(_numlen % 2 == 0)
		{
			for(int j = 0 ; j < _numlen/2;j++)
			{
				if(_num[j] != _num[_numlen-j-1])
				{
					Palind = false;
					break;
				}
			}
		}
		else
		{
			for(int j = 0 ; j < (_numlen-1)/2;j++)
			{
				if(_num[j] != _num[_numlen-j-1])
				{
					Palind = false;
					break;
				}
			}
		}
	}

	return Palind;
}
int CheckFandS( int A, int B)
{
	int counter = 0;
	int _min =0;
	int _max = 0;
	if (A < B)
	{
		_min = A;
		_max = B;
	}
	else
	{
		_min = B;
		_max = A;
	}

	for ( int i = _min ;i <= _max ;i++)
	{		
		if (i ==0)
			continue;
		int root = sqrt((float)i);
		if( (root* root) != i)
			continue;

		if(palindrome(i))
		{
			if(palindrome(root))
				counter++;
		}			
	}
	return counter;
}
void main()
{
	string line;
	ifstream myfile;
	ofstream outfile;
	myfile.open ("C:\\Users\\ahmed\\Documents\\Visual Studio 2012\\Projects\\Fair and Square\\Debug\\C-small-attempt0.in");
	outfile.open ("C:\\Users\\ahmed\\Documents\\Visual Studio 2012\\Projects\\Fair and Square\\Debug\\C-small-attempt0.out");
	
	int TestCases;
	int A[100];
	int B[100];
	int counter = 0;

	if(myfile.is_open())
	{		
		TestCases = getValue(myfile);
	
		for (int i = 0; i < TestCases;i++)
		{	
			getline(myfile,line);
			string token;
			istringstream iss(line);
			for ( int j = 0 ; j < 2; j++)
			{
				getline(iss, token, ' ');
				int value =atoi(token.c_str());
				if(j==0)
					A[i]= value;
				else
					B[i]= value;
			}			
		}

		
		if(outfile.is_open())
		{			
			for (int i=0;i<TestCases;i++)
			{
				int _FS = CheckFandS(A[i],B[i]);
				outfile<<"Case #"<<i+1<<": "<<_FS<<endl;
			}
		}
	}
	
	myfile.close();
	outfile.close();
}