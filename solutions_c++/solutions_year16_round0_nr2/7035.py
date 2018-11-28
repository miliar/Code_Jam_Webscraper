#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>

using namespace std;

string s,s1,s2,trunc;
int l,ltmp;

void reverse(int c)
{
	for(int y=(c-1);y>=0;y--)
	{
		if(s[y]=='-')
			s1=s1+'+';
		else
			s1=s1+'-';
	}
}

void trimstr()
{
	int i=l-1;
	int flag=0;
	while(i>=0)
	{
		if(s[i]=='-')
		{
			flag=1;
			s=s.substr(0,(i+1));
			break;
		}
		i--;
	}
	if(flag==0)
		s=s.substr(0,(i+1));
}

int initnum()
{
	int i=0;
	while(s[i]=='+')
		i++;
	return i;
}

int main()
{
	int t,x=0,f=0,j=0;
	scanf("%d",&t);

	for(int k=0;k<t;k++)
	{
		std::cin>>s;
		f=0;

		l=s.size();
		trimstr();
		s1=s;
		s.erase();
		s=s1;
		s1.erase();
		l=s.size();

		while(l>0)
		{
			if(s[0]=='-')
			{
				reverse(l);
				s.erase();
				s=s1;
				trimstr();
				s1=s;
				s.erase();
				s=s1;
				s1.erase();
				l=s.size();
				f++;
			}
			else
			{
				s1.erase();
				s2.erase();
				j=initnum();
				reverse(j);
				s2=s.substr(j);
				s.erase();
				s=s1+s2;
				f++;
				s1.erase();
				s2.erase();
				l=s.size();
				reverse(l);
				s.erase();
				s=s1;
				trimstr();
				s1=s;
				s.erase();
				s=s1;
				s1.erase();
				l=s.size();
				f++;
			}
		}
		std::cout<<"Case #"<<(k+1)<<": "<<f<<"\n";
	}
}