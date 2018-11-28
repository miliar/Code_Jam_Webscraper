#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int l=1; l<=t; l++)
	{
		int s;
		long long count = 0;
		string str;
		cin>>s;
		int a[s+1],standing[s+1];
		getline(cin,str);
		for(int i=0; i<=s; i++)
		{
			a[i]=str[i+1]-'0';
		}
		standing[0] = a[0];
		for(int i=1; i<=s; i++)
		{
			if(a[i]==0)
			standing[i]=standing[i-1];
			else
			{
				standing[i] = max(standing[i-1], i) + a[i];
				if(i>standing[i-1])
				count+=i-standing[i-1];
			}
		}
		cout<<"Case #"<<l<<": "<<count<<"\n";
	}
	return 0;
}