#include <fstream>
#include <iostream>
#include <math.h>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int count(int a,int b);
bool IsPalindrome(int n);

int main()
{
	fstream in;
	fstream out;
	in.open("C-small-attempt0.in", ios::in);
	out.open("output.out", ios::trunc|ios::out);

	int t,a,b;

	in>>t;
	for (int repeat = 0; repeat < t; ++repeat)
	{
		in>>a>>b;
		out<<"Case #"<<repeat+1<<": ";
		out<<count(a,b);
		out<<endl;
	}
}

int count(int a,int b)
{
	int count=0;
	for (int i = floor(sqrt(a)); i < floor(sqrt(b))+1; ++i)
	{
		int temp=i*i;
		if (temp>=a && temp<=b && IsPalindrome(temp) && IsPalindrome(i)) count++;
	}
	//cout<<endl;
	return count;
}

bool IsPalindrome(int n)
{
	stringstream ss;
	ss<<n;
	string s=ss.str();
	//cout<<s<<endl;
	if( equal(s.begin(), s.begin() + s.size()/2, s.rbegin()) ) return true;
	return false;
}