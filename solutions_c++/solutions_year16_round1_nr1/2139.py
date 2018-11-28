#include<iostream>
#include<string>
#include<stdlib.h>
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
		string s,s1;
		cin>>s;
		int n=s.length();
		s1="";
		char c=s[0];
		s1=s1+c;
		for(int i=1;i<n;i++)
		{
			c=s1[0];
			if(s[i]<c)
			{
				
				s1=s1+s[i];
				//cout<<"1"<<endl;
			}
			else
				s1=s[i]+s1;
		}
		cout<<"Case #"<<k<<": "<<s1<<endl;
	}
}
