#include <iostream>
#include <sstream>
#include <string>
#include <math.h>
#include <algorithm>
#include <cstdio>
using namespace std;
bool ispalindrome(int);
bool issquare(int);
int main()
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
	int T;
	cin>>T;
	for(int caseno=1;caseno<=T;++caseno)
	{
		int start,end,count=0;
		cin>>start>>end;
		for(int i=start;i<=end;++i)
		{
			if(ispalindrome(i)==true&&issquare(i)==true)
				++count;
		}
		cout<<"Case #"<<caseno<<": "<<count<<endl;
	}
	return 0;
}
bool ispalindrome(int key)
{
	stringstream SS;
	string sourcestr;
	string targetstr;
	SS<<key;
	SS>>sourcestr;
	if(sourcestr.size()==1)
	{
		return true;
	}
	targetstr = sourcestr;
	reverse(sourcestr.begin(),sourcestr.end());
	if(sourcestr == targetstr)
	{
		return true;
	}
	return false;
}
bool issquare(int key)
{
	int sqr = sqrt(key);
	if(sqr*sqr != key)
	{
		return false;
	}
	if(ispalindrome(sqr)==true)
	{
		return true;
	}
	return false;
}
