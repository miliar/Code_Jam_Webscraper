#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
	int t,i,j=1,e,b,c=0;
	int a[5]={1,4,9,121,484};
	ofstream fout;
	fout.open("output.txt");
	ifstream fin;
	fin.open("input.txt");
	fin>>t;
	while(t--)
	{
	 c=0;
	 fin>>e>>b;	
	 for(i=0;i<5;i++)
	 if(a[i]>=e&&a[i]<=b)
	 c++;
	 fout<<"Case #"<<j++<<": "<<c<<"\n";
	}
}
