// google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<string>
#include<map>
#include<fstream>
using namespace std;
void main()
{
	int n;
	ofstream out ("OUTPUT.txt");
	ifstream in1("A-small-attempt4.in");
	in1>>n;
	int b[10]={0};
	int *ans=new int[n];
	char a[1000000];
	for(int i=0;i<n;i++)
	{
		in1>>a;
		int  c=atoi(a);
		int c2=c;
		 int count=1;
		 for(int j=0;j<10;j++)
			 b[j]=0;

		while(true)
		{
			if(c==0){itoa(-1,a,10);break;}
		for(int j=0;j<strlen(a);j++)
		{
			b[a[j]-'0']=1;
		}
		bool fl=true;
		for(int j=0;j<10&&fl;j++)
			if(b[j]!=1)fl=false;
		if(fl)break;
		int c2=c*(count+1);	
		count++;
		itoa(c2,a,10);
		}
	ans[i]=atoi(a);
	}
	for(int i=0;i<n;i++)
	{out<<"Case #"<<i+1<<": ";
	if(ans[i]==-1)out<<"INSOMNIA"<<endl;
	else out<<ans[i]<<endl;
	}
}

