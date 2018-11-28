#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	long k,a,b,test;
	long j,l,p,count;
	ifstream fin;
	ofstream fout;
	fout.open("output.in");
	fin.open("B-small-attempt0.in");
	fin>>test;
	for(int  i=1;i<=test;i++)
	{
		count =0;
		fin>>a>>b>>k;
		for(j=0;j<a;j++)
		{
			for(l=0;l<b;l++)
			{
				if((j&l)<k)
					count++;
			}
		}
		fout<<"Case #"<<i<<": "<<count<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}
