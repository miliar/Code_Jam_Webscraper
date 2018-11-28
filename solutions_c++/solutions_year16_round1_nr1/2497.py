#include<iostream>

using namespace std;

void shift(string &str)
{
	
	str.push_back('c');
	for(int i = str.length() - 1; i > 0 ; i--)
	{
		str[i] = str[i-1];
	}
		
}		


int main()
{
	int T;
	string s[100], a[100];
	char top;
	cin>>T;
	for(int i = 0 ; i < T; i++)
	{
		cin>>s[i];
		a[i].push_back(s[i][0]);
		top = s[i][0];
		for(int j = 1; j < s[i].length(); j++)
		{
			if(top > s[i][j])
				a[i].push_back(s[i][j]);
			else
			{
				shift(a[i]);
				a[i][0] = s[i][j];
				top = s[i][j];	
			}
			
			
		}
				
	}
	for(int i = 0 ; i < T; i++)
	{
		cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
	}
		
	return 0;
}
