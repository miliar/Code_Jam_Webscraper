#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	string str[t];
	for (int i = 0; i < t; i++)
	{
		cin>>str[i];
	}
	for (int i = 0; i < t; i++)
	{
		// string str;
		
		int len=str[i].length();
		char *tab2 = const_cast<char*>(str[i].c_str());
		int j=len-1;
		while(j>=0&&tab2[j]=='+')
		{
			j=j-1;
		}
		if (j<0)
		{
			cout<<"Case #"<<i+1<<": "<<0<<endl;
			continue;
		}
			// cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			// cout<<"Case #"<<i+1<<": "<<an<<endl;
		int count=1;
		for (int k = 1; k < j+1; k++)
		{
			if (tab2[k]!=tab2[k-1])
			{
				count++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
		
	}
	return 0;
}