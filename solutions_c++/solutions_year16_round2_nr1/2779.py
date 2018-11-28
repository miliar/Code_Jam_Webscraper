#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	int T,i,j,length,ch[26],di[10],x,k;
//	std::fstream IP("input.txt", std::ios_base::in);
	std::fstream IP("A-large.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPlarge.txt", std::ios_base::out);
	for(i=0;i<T;i++)
	{
//		cout<<i<<" check\n";
		char S[2000];
		for(j=0;j<26;j++)
			ch[j]=0;
		for(j=0;j<10;j++)
			di[j]=0;
		IP>>S;
		length=strlen(S);
		for(j=0;j<length;j++)
			ch[int(S[j])-int('A')]++;
//		for(j=0;j<26;j++)
//			cout<<ch[j];
//		cout<<"hi\n";
		x=ch[int('Z')-int('A')];
		di[0]=x;
//		cout<<"hi2\n";
		ch[int('Z')-int('A')]=0;
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-x;
		ch[int('R')-int('A')]=ch[int('R')-int('A')]-x;
		ch[int('O')-int('A')]=ch[int('O')-int('A')]-x;
//		for(j=0;j<26;j++)
//			cout<<ch[j];
//		cout<<"hi11\n";
//		cout<<"hi3\n";
		x=ch[int('X')-int('A')];
		ch[int('S')-int('A')]=ch[int('S')-int('A')]-x;
		ch[int('I')-int('A')]=ch[int('I')-int('A')]-x;
		ch[int('X')-int('A')]=0;
		di[6]=x;
		x=ch[int('W')-int('A')];
		ch[int('T')-int('A')]=ch[int('T')-int('A')]-x;
		ch[int('W')-int('A')]=0;
		ch[int('O')-int('A')]=ch[int('O')-int('A')]-x;
		di[2]=x;
//		for(j=0;j<26;j++)
//			cout<<ch[j];
//		cout<<"hi5\n";
		x=ch[int('U')-int('A')];
		ch[int('F')-int('A')]=ch[int('F')-int('A')]-x;
		ch[int('O')-int('A')]=ch[int('O')-int('A')]-x;
		ch[int('R')-int('A')]=ch[int('R')-int('A')]-x;
		ch[int('U')-int('A')]=0;
		di[4]=x;
		x=ch[int('R')-int('A')];
		ch[int('T')-int('A')]=ch[int('T')-int('A')]-x;
		ch[int('H')-int('A')]=ch[int('H')-int('A')]-x;
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-2*x;
		ch[int('R')-int('A')]=0;
		di[3]=x;
		x=ch[int('G')-int('A')];
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-x;
		ch[int('I')-int('A')]=ch[int('I')-int('A')]-x;
		ch[int('H')-int('A')]=ch[int('H')-int('A')]-x;
		ch[int('T')-int('A')]=ch[int('T')-int('A')]-x;
		ch[int('G')-int('A')]=0;
		di[8]=x;
		x=ch[int('F')-int('A')];
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-x;
		ch[int('I')-int('A')]=ch[int('I')-int('A')]-x;
		ch[int('V')-int('A')]=ch[int('V')-int('A')]-x;
		ch[int('F')-int('A')]=0;
		di[5]=x;
		x=ch[int('S')-int('A')];
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-2*x;
		ch[int('N')-int('A')]=ch[int('N')-int('A')]-x;
		ch[int('V')-int('A')]=ch[int('V')-int('A')]-x;
		ch[int('S')-int('A')]=0;
		di[7]=x;
		x=ch[int('O')-int('A')];
		ch[int('E')-int('A')]=ch[int('E')-int('A')]-x;
		ch[int('N')-int('A')]=ch[int('N')-int('A')]-x;
		ch[int('O')-int('A')]=0;
//		for(j=0;j<26;j++)
//			cout<<ch[j];
//		cout<<"hi6\n";
		di[1]=x;
		x=ch[int('I')-int('A')];
		di[9]=x;		
		OP<<"Case #";
		OP<<i+1;
		OP<<": ";
		for(j=0;j<10;j++)
		{	x=di[j];
			for(k=0;k<x;k++)
				OP<<j;
		}
		OP<<"\n";
	}
	return 0;
}
