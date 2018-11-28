#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
vector<int>x;
string s1;
bool f0(string & s)
{bool c1,c2,c3,c4;
	c1=c2=c4=c3=false;
	for(int i=0;i<s.size();i++)
	{
	if(s[i]=='Z'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='E'&&c2==false)
	{s[i]='l';
		c2=true;
		;
	}
	if(s[i]=='R'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='O'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	}
		if(c1==true&&c2==true&&c3==true&&c4==true)
		{s1=s;
			return true;
		}
		else
		{
		s=s1;
		return false;
		}
}
bool f1(string &s)
{bool c1,c2,c3;
	c1=c2=c3=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='E'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='N'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='O'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	}

	if(c1==true&&c2==true&&c3==true)
		{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f2(string& s)
{bool c1,c2,c3;
	c1=c2=c3=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='T'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='W'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='O'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	}

	if(c1==true&&c2==true&&c3==true)
				{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f5(string &s)
{bool c1,c2,c3,c4;
	c1=c2=c3=c4=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='F'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='I'&&c2==false)
	{s[i]='l';
		c2=true;
	
	}
	if(s[i]=='V'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='E'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	}
if(c1==true&&c2==true&&c3==true&&c4==true)
				{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f3(string &s)
{bool c1,c2,c3,c4,c5;
	c1=c2=c3=c4=c5=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='T'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='H'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='R'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='E'&&c4==false)
	{s[i]='l';
		c4=true;
	}
	if(s[i]=='E'&&c5==false)
	{s[i]='l';
		c5=true;
		
	}
	}

if(c1==true&&c2==true&&c3==true&&c4==true&&c5==true)
			{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f4(string &s)
{bool c1,c2,c3,c4;
	c1=c2=c3=c4=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='F'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='O'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='U'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='R'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	}
if(c1==true&&c2==true&&c3==true&&c4==true)
				{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f6(string & s)
{bool c1,c2,c3;
	c1=c2=c3=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='S'&&c1==false)
	{s[i]='l';
		c1=true;
			
	}
	if(s[i]=='I'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='X'&&c3==false)
	{s[i]='l';
		c3=true;
			
	}
	}
if(c1==true&&c2==true&&c3==true)
				{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f7(string &s)
{bool c1,c2,c3,c4,c5;
	c1=c2=c3=c4=c5=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='S'&&c1==false)
	{s[i]='l';
		c1=true;
	
	}
	if(s[i]=='E'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='V'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='E'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	if(s[i]=='N'&&c5==false)
	{s[i]='l';
		c5=true;
		
	}
	}

	if(c1==true&&c2==true&&c3==true&&c4==true&&c5==true)
			{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f8(string &s)
{bool c1,c2,c3,c4,c5;
	c1=c2=c3=c4=c5=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='E'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='I'&&c2==false)
	{s[i]='l';
		c2=true;
	
	}
	if(s[i]=='G'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='H'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	if(s[i]=='T'&&c5==false)
	{s[i]='l';
		c5=true;
		
	}
	}

	if(c1==true&&c2==true&&c3==true&&c4==true&&c5==true)
			{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
bool f9(string  &s)
{bool c1,c2,c3,c4;
	c1=c2=c3=c4=false;
	for(int i=0;i<s.size();i++)
	{
	
	if(s[i]=='N'&&c1==false)
	{s[i]='l';
		c1=true;
		
	}
	if(s[i]=='I'&&c2==false)
	{s[i]='l';
		c2=true;
		
	}
	if(s[i]=='N'&&c3==false)
	{s[i]='l';
		c3=true;
		
	}
	if(s[i]=='E'&&c4==false)
	{s[i]='l';
		c4=true;
		
	}
	}

	if(c1==true&&c2==true&&c3==true&&c4==true)
			{s1=s;
			return true;
	}
		else
		{
		s=s1;
		return false;
		}
}
int main() {
	ofstream out("output.txt");
	int i=1;
	ifstream inp("input.txt");
	string s;
	int t;
	inp>>t;
	while(t!=0)
	{
	inp>>s;
	s1=s;
	while(f0(s))
		x.push_back(0);
	while(f8(s))
		x.push_back(8);
	while(f6(s))
		x.push_back(6);
	while(f2(s))
		x.push_back(2);
	while(f7(s))
		x.push_back(7);
		while(f5(s))
		x.push_back(5);
		while(f4(s))
		x.push_back(4);
		while(f3(s))
		x.push_back(3);
		while(f9(s))
		x.push_back(9);
	while(f1(s))
		x.push_back(1);	
	
	
	out<<"Case #"<<i<<": ";
	sort(x.begin(),x.end());
	for(int k=0;k<x.size();k++)
		out<<x[k];
	out<<endl;
	x.clear();
	i++;
	t--;
	}

}