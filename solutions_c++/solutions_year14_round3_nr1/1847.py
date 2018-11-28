#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		string a;
		cin>>a;
		unsigned pos = a.find("/");         // position of "live" in str
		string str1 = a.substr (0,pos);
		string str2 = a.substr (pos+1);   
		int p=stoi(str1);
		int q=stoi(str2);
		int n=q;
		int j=0;
		int x=p;
		while(n%2==0)
		{
			n=n/2;
			j++;
		}
		while(x/2>=1)
		{
			x=x/2;
			j--;
		}
		if(n!=1 || p>q)
		{
			cout<<"Case #"<<i<<": impossible"<<endl;
			continue;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<j<<endl;
		}
	}
}
