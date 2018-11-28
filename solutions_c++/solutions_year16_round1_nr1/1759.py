#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int cases=1;cases<=t;cases++)
	{
		string error;
		cin>>error;
		list<char> temp;
		temp.push_back(error[0]);
		for(int i=1;i<error.length();i++)
		{
			if(error[i]>=temp.front())
				temp.push_front(error[i]);
			else temp.push_back(error[i]);
		}
		printf("Case #%d: ",cases);
		for(list<char> :: iterator it=temp.begin();it!=temp.end();it++)
			cout<<*it;
		cout<<endl;
	}
}