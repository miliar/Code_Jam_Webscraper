#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#define lli long long int
#define vi vector <lli>
using namespace std;
fstream coutf;

string genstring(lli n, int l) //Converts number to base 2, adds 1 at beginning and end
{
	string s="1";
	for(int i=0;i<l;i++)
	{
		int r=n%2;
		s=(char) (r+'0') + s;
		n=n/2;
	}
	s="1"+s;
	return s;
}

lli convertstring(string s, int b)
{
	lli ans=0;
	int k=0;
	while(k<s.length())
	{
		int r=(int) (s[k]-'0');
		//i=i/10;
		ans= ans + r*pow(b,s.length()-1-k);
		k++;
	}
	return ans;
}

lli allperms(int l2, int p2)
{
	int l=l2/2;
	int k=l-2;
	int p=p2; //p=pow(2,k);
	int i;
	for(i=0;i<p;i++)
	{
		string s=genstring(i,l-2);
		cout<<s<<s<<" ";		
		for(int i2=2;i2<=10;i2++) 
		{
			lli permi=convertstring(s,i2); 
			cout<<permi<<" ";
		}
		cout<<endl;
	}
}

int main()
{
	//fstream coutf;
	coutf.open("Bsmall.txt");
	int t; cin>>t;
	int i,k;
	cin>>i>>k;
	allperms(i,k);
}
