#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		string str;
		int count=0;
		cin>>str;
		for(int i=0;i<str.size()-1;i++)
		{
			if(str[i]=='-' && str[i+1]=='+')
			{
				count++;
			}
			else if(str[i]=='+' && str[i+1]=='-')
			{
				count++;
			}
		}
		if(str[str.size()-1]=='-')count++;
		cout<<"Case #"<<j<<": "<<count<<"\n";
	}
	return 0;
}