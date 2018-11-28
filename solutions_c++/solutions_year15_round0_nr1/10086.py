#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,q=1;
	cin>>t;
	while(t--)
	{
		int n,i,sum=0,ct=0;
		cin>>n;
		string s;
		cin>>s;
		sum=s[0]-'0';
		for(i=1;i<=n;i++){
			if(i>sum)
			{ct+=(i-sum);
			sum+=s[i]-'0'+i-sum;}
			else
			sum+=s[i]-'0';
		}
		cout<<"Case #"<<q++<<": "<<ct<<endl;
	}
	return 0;
}
