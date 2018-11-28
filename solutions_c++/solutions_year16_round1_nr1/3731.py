#include<iostream>
#include<malloc.h>
#include<fstream>
#include<stdio.h>
#define FL(i,N) for(int i=0;i<N;i++)
using namespace std;
int main()
{
	ifstream infile;
	infile.open("A-large.in");
	int T;
	infile>>T;
	ofstream outfile;
	outfile.open("A-large-output.in");
	FL(l,T)
	{
		char str[1000];
		infile>>str;
		for(int i=0;str[i]!='\0';i++)
		{
			if(str[i]>=str[0])
			{
				char temp=str[i];
				for(int j=i-1;j>=0;j--)
				{
					str[j+1]=str[j];
				}
				str[0]=temp;
			}
		}
		
		outfile<<"Case #"<<l+1<<": "<<str<<endl;
	}
}

//cout<<"Case #"<<l+1<<": "<<ans<<endl;
