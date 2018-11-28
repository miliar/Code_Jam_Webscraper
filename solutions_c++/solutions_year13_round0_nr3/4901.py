#include <iostream>
#include<fstream>
#include <string>
#include <sstream>
#include <stack>
#include <vector>
#include <stdio.h>
#include <math.h>
using namespace std; 

bool check_fair(int x);
bool check_square(int x);
int main()
{
	int T; 
	ifstream fin("C-small-attempt0.in");
	ofstream fout;
	fout.open("Fair_square.out");
	fin >> T ; 
	for(int ii = 0 ; ii < T ; ii++)
	{   int A,B; 
	    fin>>A>>B;
		int result = 0 ;
		for(int i = A ; i <= B ; i++)
		{
			if(check_fair(i))
			{
				if(check_square(i))
				{
					result++;
				}
			}
		}
		fout<<"Case #"<<ii+1<<": "<<result<<endl;
	}
	return 0 ;
}
bool check_fair(int x)
{
string Result;          // string which will contain the result
ostringstream convert;   // stream used for the conversion
convert << x;      // insert the textual representation of 'Number' in the characters in the stream
Result = convert.str(); // set 'Result' to the contents of the stream
stack<char> temp;
	for(int i = 0 ; i < Result.size() ; i++)
	{
		temp.push(Result[i]);
	}
	string xx;	
	for(int i = 0 ; i < Result.size() ; i++)
	{
		xx.push_back(temp.top());
		temp.pop();
	}
	if(Result== xx)
	return true;
	else return false;
}

bool check_square(int x)
{
	int temp = sqrt(x);
	if (temp*temp == x) 
	{
		if(check_fair(temp))
	return true;
		else return false;
	}
	else return false; 
}