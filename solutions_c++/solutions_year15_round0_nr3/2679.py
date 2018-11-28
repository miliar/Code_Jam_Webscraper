#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
fstream fin,fout;
char str[10010];
char S[10010];
int flag=0;
int I[10010];
int K[10010];
struct node
{
	char chr;
	int minus;
	int tag;
}ARR[10010];
char eval(char a,char b)
{
	if(a=='i'&&b=='j')
	{
		return 'k';
	}
	if(a=='j'&&b=='k')
	{
		return 'i';
	}
	if(a=='k'&&b=='i')
	{
		return 'j';
	}
	if(a=='j'&&b=='i')
	{
		flag=(flag+1)%2;
		return 'k';
	}
	if(a=='k'&&b=='j')
	{
		flag=(flag+1)%2;
		return 'i';
	}
	if(a=='i'&&b=='k')
	{
		flag=(flag+1)%2;
		return 'j';
	}
	if(a=='i'&&b=='i')
	{
		flag=(flag+1)%2;
		return '$';
	}
	if(a=='j'&&b=='j')
	{
		flag=(flag+1)%2;
		return '$';
	}
	if(a=='k'&&b=='k')
	{
		flag=(flag+1)%2;
		return '$';
	}
}
int main()
{
	fin.open("in.cpp");
	fout.open("output.cpp");
	int t,L,X;
	fin>>t;
	for(int j=1;j<=t;j++)
	{
		flag=0;
		strcpy(str,"");
		fin>>L>>X;
		fin>>S;
		for(int i=0;i<X;i++)
		{
			strcat(str,S);
		}
//		cout<<str<<endl;
		int iptr=0,kptr=0;
		int len=strlen(str);
		char ch='$';
		int tag1=0;
		for(int i=0;i<len;i++)
		{
			if(ch=='$')
			ch=str[i];
			else
			ch=eval(ch,str[i]);
			if(ch=='i'&&!flag)
			{
				I[iptr++]=i;
				tag1=1;
			}
			ARR[i].chr=ch;
			ARR[i].minus=flag;
			ARR[i].tag=tag1;
			
		}
		flag=0;
		ch='$';
		int tag2=0;
		fout<<"Case #"<<j<<": ";
		for(int i=len-1;i>=1;i--)
		{
			if(ch=='$')
			ch=str[i];
			else ch=eval(str[i],ch);
			if(ch=='k'&&!flag)
			{
				if(ARR[i-1].chr=='k'&&ARR[i-1].minus==0&&ARR[i-1].tag==1)
				{
					fout<<"YES\n";
					tag2=1;
					break;
				}
			}
		}
		if(!tag2)
		fout<<"NO\n";
	}
}
