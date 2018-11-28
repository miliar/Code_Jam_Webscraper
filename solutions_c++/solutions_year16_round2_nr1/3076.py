#include <cstring>
#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

int main()
{
	int c[10];
	ifstream fin("A-large.in",ios::in);
	ofstream fout("codejam2.txt",ios::out);
	//int output[100000];
	int count[10];
	int t,k;
	string s;
	int counter=0;
	fin>>t;
	while(t--)
	{
	fin>>s;
	k=0;
	for(int i=0;i<10;i++){
		count[i]=0;
		c[i]=0;
}
counter++;
fout<<"Case #"<<counter<<": ";
	for(int i=0;i < s.length();i++)
	{
		if(s[i]=='Z')
		{
			(count[0])++;

		}
		else if(s[i]=='W')
		{
			(count[2])++;
		}
		else if(s[i]=='U')
		{
			(count[4])++;
		}
		else if(s[i]=='X')
		{
			(count[6])++;
		}
		else if(s[i]=='G')
		{
			(count[8])++;
		}
	}
	for(int i=0;i<s.length();i++)
	{
		if(s[i]=='O')
			c[1]++;
		else if(s[i]=='F')
			c[2]++;
		else if(s[i]=='S')
			c[3]++;
		else if(s[i]=='R')
			c[0]++;
		else if(s[i]=='E')
			c[4]++;
	}
	count[1]=c[1]-count[0]-count[2]-count[4];
	count[3]=c[0]-count[0]-count[4];
	count[5]=c[2]-count[4];
	count[7]=c[3]-count[6];
	count[9]=c[4]-count[0]-count[1]-(count[3]*2)-count[5]-(count[7]*2)-count[8];
	for(int i=0;i<10;i++)
	{
		while(count[i]!=0)
		{
			fout<<i;
			count[i]--;
		}
	}
	fout<<"\n";
	}
	return 0;
} 