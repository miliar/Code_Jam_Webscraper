#include <iostream>
using namespace std;

int main() {
	// your code goes here
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int m=1; m<=t; m++)
	{
		int count = 0;
		string s;
		cin>>s;
		int l = s.length();
		char prev = '+';
		for(int i=l-1; i>=0; i--)
		{
			if(prev != s[i])
			{
				count++;
				prev = s[i];
			}
		}
		cout<<"Case #"<<m<<": "<<count<<"\n";
	}
	return 0;
}