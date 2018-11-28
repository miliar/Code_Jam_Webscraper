#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int cases = 1;
	while(t--)
	{
		int sm;
		cin>>sm;
		string s;
		cin>>s;
		int standing = 0;
		int required = 0;
		for(int i=0;i<=sm;i++)
		{
			int num = s[i]-'0';
			if(standing >= i)
			{
				standing += num;
			}
			else
			{
				required = required + (i-standing);
				standing += (i-standing) + num;
			}
		}
		cout<<"Case #"<<cases<<": "<<required<<"\n";
		cases++;
	}
	
	return 0;
}