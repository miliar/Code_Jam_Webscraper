#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
int main()
{
	int T,i,j,length;
	int op;
//	std::fstream IP("input.txt", std::ios_base::in);
	std::fstream IP("B-large.in", std::ios_base::in);
	IP>>T;
	std::fstream OP("OPlarge.txt", std::ios_base::out);
	for(i=0;i<T;i++)
	{
		char S[100];
		op=0;
		IP>>S;
		length=strlen(S);
		for(j=1;j<length;j++)
			if(S[j]!=S[j-1])
				op++;
		if((S[0]=='+')&&(op%2==1))
			op++;
		if((S[0]=='-')&&(op%2==0))
			op++;
		OP<<"Case #";
		OP<<i+1;
		OP<<": ";
		OP<<op;
		OP<<"\n";
	}
	return 0;
}
