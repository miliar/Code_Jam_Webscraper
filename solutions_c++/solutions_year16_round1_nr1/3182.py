#include <iostream>
#include<string>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int r=1;
	while(r<=t)
	{
		string s;
		cin>>s;
		int n=s.length();
		string res; res=s[0];
		for(int i=1;i<n;i++)
		{
			if(res[0]<=s[i])
			res=s[i]+res;
			else
			res=res+s[i];
		}
		cout<<"Case #"<<r<<": "<<res<<"\n";
		r++;
	}
	return 0;
}