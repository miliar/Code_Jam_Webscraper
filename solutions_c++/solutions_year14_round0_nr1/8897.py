#include<iostream>
#include<fstream>
using namespace std;
struct
{
	int x;
	int y;
}s[16];
int main()
{
	ifstream fin("A-small-attempt1.in");
	ofstream fout("Output1.txt");
	int T,n,p,q,count=0,no;
	fin>>T;
	for(int j=0;j<T;j++)
	{
		count=0;
	fin>>p;
	for(int i=0;i<16;i++)
	{
		fin>>n;
		s[n-1].x=i/4+1;
	}
	fin>>q;
	for(int i=0;i<16;i++)
	{
		fin>>n;
		s[n-1].y=i/4+1;
	}
	for(int i=0;i<16;i++)
	{
		if((s[i].x==p)&&(s[i].y==q))
		{no=i+1;
		 count++;
		}
	}
	if(count==1)
	fout<<"Case #"<<j+1<<": "<<no<<endl;
	else
	if(count==0)
	fout<<"Case #"<<j+1<<": "<<"Volunteer cheated!\n";
	else
	fout<<"Case #"<<j+1<<": "<<"Bad magician!\n";
	}
	
	
}
