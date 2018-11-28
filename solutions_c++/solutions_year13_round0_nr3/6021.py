#include <iostream>
#include <fstream>
#include <math.h>
#include <stack>

#define INFILE "C:\\GCJ\\CodeJam\\input_output\\C-small-attempt0.in"
#define OUTFILE "C:\\GCJ\\CodeJam\\input_output\\Csmall.out"
using namespace std;


bool IsPalindrome(__int64 n)
{
	int digits = 0;
	__int64 n1 = n;
	for(int i = 1; i<20; i++)
	{
		if(n1/(10) == 0)
		{
			digits = i;
			break;
		}
		n1 = n1/(10*i);
	}

	stack <int>dig;
	n1 = n;
	for(int i = 1; i<=digits; i++)
	{
		dig.push(n1%10);
		n1 = n1/(10);
	}
	for(int i = 1; i<=digits; i++)
	{
		if((n%10) != dig.top())
			return false;
		dig.pop();
		n = n/(10);
	}
	return true;

}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open(INFILE);
	if(!fin.is_open())
	{
		cout<<"Failed to open input file. Press a key to exit...";
		cin.get();
		return 0;
	}
	fout.open(OUTFILE);
	if(!fin)
	{
		cout<<"Failed to open output file. Press a key to exit...";
		cin.get();
		return 0;
	}	
	// Actual code starts
	//===================
	int totalcases = 0;
	fin>>totalcases;
	
	cout<<"\nReading total cases: "<<totalcases;
	for( int c= 1; c<= totalcases; c++)
	{
		__int64 count = 0;
		fin.get(); // get new line
		fout<<"Case #"<<c<<": ";

		__int64 start = 0;
		__int64 end = 0;

		fin>>start;
		fin.get();
		fin>>end;

		__int64 smallestRoot = (__int64)sqrt((double)start);
		if(smallestRoot*smallestRoot < start)
			smallestRoot++;
		
		for(__int64 root = smallestRoot, num = root*root; num <= end; root++, num = root*root)
		{
			if(IsPalindrome(root))
			{				
				if(IsPalindrome(num))
				{
					count++;
				}
			}
		}
		fout<<count<<"\n";
	}

		
	//===================
	// Actual code ends
	if(fin)
	{
		fin.close();
	}
	if(fout)
	{
		fout.close();
	}
	cout<<"\nExiting program. Press a key to exit...";
	cin.get();
	return 0;
}
