#include<iostream>
#include <string>
#include <bitset>
#include <limits>
#include<math.h>
#include<cmath>
#include<fstream>
#include<bitset>
#include<vector>
#include <sstream>
#include<algorithm>
#include<time.h>
#include<set>
#include<map>
#include <numeric>
//#include "Source.cpp"
using namespace std;

int convert(string s)
{
	int val;
	stringstream t(s);
	t>>val;
	return val;
}
string ToString(int x)
{
	stringstream ss;
	ss<<x;
	string s=ss.str();
		return s;
}
bool Palindrome(int x)
{
	string org=ToString(x);
	string rev=org;
	std::reverse(rev.begin(),rev.end());
	if(org==rev)
		return true;
	else
		return false;
}
bool valid(int x)
{
	double t=sqrt(x);
	
	double mod=fmod(t,1.0);
	if(mod==0)
	return true;
	else return false;
}
bool isFair(int x)
{
	if(Palindrome(x))
	{
		
		if(valid(x))
		{
			x=sqrt(x);
			if(Palindrome(x))
			return true;
			else
			return false;
		}
		else
			return false;
	}
	else
		return false;
}

int find(int min , int max)
{
	int count=0;
	for (int i = min; i <= max; i++)
	{
		if(isFair(i))
		{
			count++;
		}
	}
	return count;
}
int main()
{
	cout<<isFair(1000)<<endl;
	
	int Testcase;
	
	 string STRING;
	ifstream infile;
	infile.open ("C-small-attempt0.in");
	ofstream Result;
Result.open("Result.txt");
string Test;
getline(infile,Test);
int TestCases;
Testcase=convert(Test);

for (int i = 0; i < Testcase; i++)
{
	int x=i;
	int minval;
	int maxval;
		
	getline(infile,STRING);
	vector<int> size;
	int t;
	stringstream sizeline(STRING);
	while (sizeline>>t)
	{
		size.push_back(t);
	}
	minval=size[0];
	maxval=size[1];

	Result<<"Case #"<<++x<<": "<<find(minval,maxval)<<endl;
	size.clear();
}
	return 0;
}