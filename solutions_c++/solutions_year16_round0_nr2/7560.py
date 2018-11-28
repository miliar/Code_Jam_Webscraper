#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//A-small-attempt0.in","r",stdin);
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//abhishek.txt","w",stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<k<<": ";
		int n=s.length(),c=0;
		for(int i=1;i<n;i++)
		{
			if(s[i]!=s[i-1])
				c++;
		}
		if(s[n-1]=='-')
			c++;
		cout<<c<<endl;	
	}
}
