#include<bits/stdc++.h>
using namespace std;
int  main()
{
	ifstream f1("A-large.in");
	ofstream f2("Ans-A.txt");
	int t,x=1;
	f1>>t;
	while(t--)
	{
	f2<<"Case #"<<x++<<": ";
	string s;
	f1>>s;
	string k;
	k+=s[0];
	for(int i=1;s[i]!='\0';i++)
	{
		
		if(s[i]<k[i-1])
			k+=s[i];
		else if(s[i]>=k[0])
		{
			string l=s[i]+k;
			k=l;
		}
		else k+=s[i];
	}
	//k[i]='\0';
	f2<<k<<'\n';
	}
}
