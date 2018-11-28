#include<iostream>
using namespace std;
#include<fstream>
#include<cmath>
#include<string>

int Maxcf(int a,int b)
{
	if(b%a==0)
		return a;
	if(a<b)
		b=b%a;
	while(1)
	{
		if(a%b==0)
			return b;
		else
			a=a%b;
		if(b%a==0)
			return a;
		else
			b=b%a;
	}
	return 0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("F:\\A-small-attempt0.in");
	fout.open("F:\\A-small-attempt0.out");
	int t;
	fin>>t;
	int a,b;
	for(int n=1;n<=t;n++)
	{
		bool out=false;
		string s;
		fin>>s;
		a=atoi(s.substr(0,s.find('/'-1)).c_str());
		b=atoi(s.substr(s.find('/')+1).c_str());
		int maxcf=Maxcf(a,b);
		if(a>b)
		{
			fout<<"Case #"<<n<<": impossible"<<endl;
			continue;
		}
		a/=maxcf;
		b/=maxcf;
		int g=0;
		while(b!=1)
		{
			if(b%2==1)
			{
				fout<<"Case #"<<n<<": impossible"<<endl;
				out=true;
				break;
			}
			if(b>=a)
				g++;
			b/=2;
		}
		if(!out)
			fout<<"Case #"<<n<<": "<<g<<endl;
	}
	return 0;
}