#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int test=1,test0;
	cin>>test0;
	while(test0--)
	{
		cout<<"Case #"<<test++<<": ";
		char s[1000]={0};
		cin>>s;
		int n=strlen(s),c=0;
		for(int i=n-1;i>=0;i--)
			if(s[i]=='-')break;
			else s[i]=0;
		n=strlen(s);
		if(n==0){cout<<0<<endl;continue;}
		for(int i=0;i<n;i++)
		{
			while(i+1<n && s[i]==s[i+1])i++;
			c++;
		}
		cout<<c<<endl;
	}
	return 0;
}