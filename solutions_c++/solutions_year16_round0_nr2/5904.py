#include <iostream>
#include <string>

using namespace std;

int funct(string s)
{
	int counter;
	if(s[0] == '+')
		counter = 0;
	else
		counter = 1;
	for(int i = 1; i<s.size(); i++)
	{
		if(s[i] == '-'  && s[i-1] == '+')
			counter = counter + 2;
	}
	return counter;
}

int main()
{
	int t;
	cin>>t;
	int i = 1;
	while(t--)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i<<": "<<funct(s)<<endl;
		i++;
	}
}