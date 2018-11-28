#include<iostream>
#include<fstream>
#include<string.h>
#include<stdlib.h>
using namespace std;
int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
	int T,num=1,s_max,f=0,sum=0;
	string ar;
	fin>>T;
	while(T--)
	{
		fin>>s_max;
		getline(fin,ar);
		sum=ar[1]-48;
		for(int i=2;i<=s_max+1;i++)
		{
			if(sum<(i-1)){f++;sum=sum-(ar[i-1]-48);ar[i-1]=i-1-sum+48;sum=sum+ar[i-1]-48;}
			sum=sum+ar[i]-48;
		}
		fout<<"Case #"<<num<<": "<<f<<"\n";
		num++;f=0;
	}
	return 0;
}
