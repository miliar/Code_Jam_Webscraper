#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i, j, ans=0, T;
	cin>>T;
	string s;
	for(int k=1; k<=T; ++k)
	{
		cin>>s;
		cout<<"Case #"<<k<<": ";
		int n=s.length();
		int m=0;
		for(i=0; i<n-1; ++i)
		{
			m++;
			while(s[i]==s[i+1] && i<n-1)
				i++;
		}
		if(s[n-1]!=s[n-2])
			m++;
		if(s[n-1]=='+')
			cout<<m-1<<endl;
		else
			cout<<m<<endl;
	}
	return 0;
}