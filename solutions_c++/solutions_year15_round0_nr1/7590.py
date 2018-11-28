#include<iostream>
#include<fstream>
using namespace std;
int main()
{

	ofstream fout;
	fout.open("output.txt");
	ifstream fin;
	fin.open("input.txt");
	int t;
	fin>>t;
	
	for(int j=0;j<t;j++)
	{
	
		int smax,n;
		fin>>smax;
		string s;
		fin>>s;
		int m=0,k=0;
		for(int i=0;i<smax+1;i++)
		{
			if((k-i)<0)
			{
				m++;
				k++;
			}
			if((s[i]-'0')!=0)
			{
				
				k=k+(s[i]-'0');
			}
		}
		fout<<"Case #"<<j+1<<": "<<m<<"\n";
	}
}
