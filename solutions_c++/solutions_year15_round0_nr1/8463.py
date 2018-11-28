#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{	int n;
	ifstream fin("a.in");
	ofstream fout("a.out");
	fin>>n;
	
	int n1,l,sum,sum2;
	string s1;
	for(int i=0;i<n;i++)
	{
	
	fin>>n1>>s1;
	sum=0;
	sum2=0;
	l=s1.length();
		for(int j=0;j<l;j++)
		{	
			if(s1[j]>'0'&&sum<j)
			{	sum2+=(j-sum);
				sum=sum+(j-sum);		
			}
			sum=sum+s1[j]-'0';
		}
	fout<<"Case #"<<(i+1)<<": "<<sum2<<"\n";	
	}
}
