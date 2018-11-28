#include <iostream>
#include <string>
using namespace std;


int solve(string str)
{
	//Find the reduced form
	int pos, neg;

	while(1)
	{
		pos=str.find("++");
		if(pos != string::npos)
		{
			str.replace(pos, 2, "+");
		}
		else
		{
			break;
		}
	}
	while(1)
	{
		neg=str.find("--");
		if(neg != string::npos)
		{
			str.replace(neg, 2, "-");
		}
		else
		{
			break;
		}
	}

	//transformation
	int n = str.length();
	if(str[n-1]=='+')
		return n-1;
	else
		return n;
}

int main()
{
	int T;
	cin>>T;
	string str;

	for(int t = 0; t < T; t++)
	{
		cin>>str;
		cout<<"Case #"<<t + 1<<": "<<solve(str)<<endl;
	}
	system("pause");
	return 0;
}