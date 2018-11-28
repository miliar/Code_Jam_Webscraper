#include <iostream>
#include <string>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
	
	ofstream out("B-large.txt");
	string s;
	bool op = false;
	int count=0;
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
	cin >> s;
	for(int i=s.length()-1;i>=0;i--)
	{
	if(s[i]=='-')
	for(int j=i;j>=0;j--)
	{
		if(s[j]=='-')
		s[j]='+';
		else
		s[j]='-';
		op = true;
	}
	if(op)
	count++;
	op = false;
	}
	out<<"Case #"<<k+1<<": "<<count<<"\n";
	count=0;
	}
} 
