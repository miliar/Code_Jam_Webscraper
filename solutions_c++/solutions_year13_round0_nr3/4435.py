#include <stdio.h>
#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
using namespace std;
bool ishuiwen(long x);
int main()
{
	ifstream input("C-small-attempt1.in");
	ofstream out("a.out");
	int T;
	input>>T;
	for(int i=0;i<T;i++)
	{
		long A,B;
		input>>A>>B;
	int cout=0;
	long a=(long)ceil(sqrt((double)A));
	long b=(long)floor(sqrt((double)B));

	for(long c=a;c<=b;c++)
	{
		if(ishuiwen(c*c)&&ishuiwen(c))
			cout++;	
	}
	out<<"Case #"<<i+1<<": "<<cout<<endl;

	}
	input.close();
	out.close();
	return 0;
}
bool ishuiwen(long x)
{
	string s;
	char a[1000];
	ltoa(x,a,10);
	s=a;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!=s[s.length()-1-i])
			return false;
	}

	return true;
}