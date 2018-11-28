#include "MatchHead.h"

#ifdef FRSQ

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;

	ifstream in;
	ofstream out;

void multiply(const char *a,const char *b, char *c, int ca, int cb)
{
	int i,j;
	char *s;
	s = new char[ca+cb];
	memset(s,0,(ca+cb));// 每个元素赋初值0
	
	for (i=0;i<ca;i++)
		for (j=0;j<cb;j++)
			s[i+j+1]+=(a[i]-'0')*(b[j]-'0');
	
	for (i=ca+cb-1;i>=0;i--)
		if (s[i]>=10)
		{
			s[i-1]+=s[i]/10; 
			s[i]%=10;
		}
	
	i=0;
	while(s[i]==0) i++;// 跳过头部0元素
	for (j=0;i<ca+cb;i++,j++) c[j]=s[i]+'0';
	c[j]='\0';
	delete s;
}

void square(const char input[], int length, char output[])
{
	::multiply(input, input, output, length, length);
}

int compare(const char s1[], const char s2[], int l1, int l2)
{
	if(l1 > l2)return 1;
	if(l2 > l1)return -1;
	for(int i = 0; i < l1; i ++)
	{
		if(s1[i] > s2[i])return 1;
		if(s1[i] < s2[i])return -1;
	}
	return 0;
}

int nextpldrm(char s[], int length)
{
	if(length % 2)
	{
		for(int i = 0; i <= length / 2 ; i ++)
		{
			char c = s[length/2+i];
			if(c != '9')
			{
				s[length/2+i] ++;
				s[length/2-i] = s[length/2+i];
				return length;
			}
			else
			{
				s[length/2+i] = '0';
				s[length/2-i] = '0';
			}
		}
		s[0] = '1';
		s[length] = '1';
		length ++;
		return length;
	}
	else
	{
		for(int i = 0; i <= length / 2 ; i ++)
		{
			char c = s[length/2+i];
			if(c != '9')
			{
				s[length/2+i] ++;
				s[length/2-1-i] ++;
				return length;
			}
			else
			{
				s[length/2+i] = '0';
				s[length/2-1-i] = '0';
			}
		}
		s[0] = '1';
		s[length] = '1';
		length ++;
		return length;
	}
}

void nearestpldrm(const char input[], char output[], int length)
{
	int l = (length - 1) /2;
	for(int i = 1; i < l; i ++)
	{
		output[i] = '0';
	}
	if(length % 2)
	{
		output[0] = '1';
		output[l] = '1';
	}
	else
	{
		output[0] = '3';
		output[l] = '3';
	}
	l ++;
	while(1)
	{
		char sq[100];
		memset(sq,0,100);
		::square(output, l, sq);
		if(::compare(sq, input, strlen(sq), length) >= 0)return;
		l = nextpldrm(output, l);
	}
}

bool checkpldrm(const char s[], int length)
{
	int i,j;
	if(length % 2)
	{
		for(i = 0, j = length -1; i != j; i ++, j --)
		{
			if(s[i] != s[j])return false;
		}
	}
	else
	{
		for(i = 0, j = length -1; i < j; i ++, j --)
		{
			if(s[i] != s[j])return false;
		}
	}
	return true;
}

int main(int argc, char* argv[])
{
	in.open("1.txt");
	out.open("out.out");

	string snum;
	getline(in,snum);
	int num;
	sscanf(snum.c_str(),"%d", &num);
	for(int l = 0; l < num; l ++)
	{
		string str;
		char sa[100], sb[100];
		char sc[100];
		memset(sa,0,100);
		memset(sb,0,100);
		memset(sc,0,100);
		getline(in, str);
		sscanf(str.c_str(),"%s %s",sa, sb);
		int la = strlen(sa);
		int lb = strlen(sb);

		::nearestpldrm(sa, sc, la);

		int counter = 0;

		while(1)
		{
			char sd[100];
			memset(sd, 0, 100);
			int lc = strlen(sc);
			square(sc, lc, sd);
			int ld = strlen(sd);
			if(compare(sd,sb,ld,lb) == 1)break;
			if(checkpldrm(sd, ld)) counter ++;
			::nextpldrm(sc, lc);
		}
		out << "Case #" << l+1 << ": " << counter << endl;
	}

	in.close();
	out.close();
	return 0;
}

#endif