#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	int t,i;
	ifstream fin;
	fin.open("A-large.in");
	fin>>t;
	ofstream outfile;
	outfile.open("output.in");
	for(i=0;i<t;i++)
	{
		int s,mem=0;
		fin>>s;
		int cum[s];
		char str[s+1];
		fin>>str;
		cum[0]=str[0]-'0'-1;
		if(cum[0]==-1)
		mem++;
		for(int j=1;j<=s;j++)
		{
			cum[j]=str[j]-'0'-1;
			if(cum[j-1]>0)
			cum[j]+=cum[j-1];
			if(cum[j]<0)
			mem++;
		}
		outfile<<"Case #"<<i+1<<": "<<mem<<"\n";
	}
}
