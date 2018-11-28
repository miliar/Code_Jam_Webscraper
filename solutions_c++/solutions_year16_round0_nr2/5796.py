#include <iostream>
#include <string>

using namespace std;

typedef long long llong;

void operate(string &s)
{
	int i = 0;
	while(s[i]==s[0]) i++;
	string str1;
	string str2 = s.substr(i);
	if(s[0]=='+')
	{
		str1.assign(i, '-');
	}
	else
	{
		str1.assign(i, '+');
	}
	s = str1 + str2;
}

int countIt(string s)
{
	int i=0;
	while(s.find('-')!=string::npos)
	{
		operate(s);
		i++;
	}
	return i;
}

int main()
{
	int t;
	string s;
	cin >> t;
	for(int i=1; i<=t; i++)
	{
		cin >> s;
		cout<< "Case #" << i << ": " << countIt(s) << endl;
	}
}