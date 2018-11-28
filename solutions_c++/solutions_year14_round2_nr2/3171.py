//============================================================================
// Name        : QB.cpp
// Author      : Chandan K Singh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class ca {
	public :
	static int andS[1000][1000];
	static int ia,jb;
	int a,b,k,count;

	ca (ifstream& v, ofstream& o, int j)
	{
		v>>a;
		v>>b;
		v>>k;
		count=0;
		if (j==0)
		{
			ia=0;
			jb=0;
		}
		if (a>ia)
		{
			for (int i=ia;i<=a;i++)
			{
				for(int j=0;j<=1000;j++)
				{
					andS[i][j]=i&j;
				}
			}
		}
		else if (a==ia && b>jb)
		{
			for (int i=jb;i<=jb;i++)
			{
				andS[ia][i]=ia&i;
			}
		}

		for (int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if (andS[i][j]<k)
				{
					count++;
				}
			}
		}
		o<<"Case #"<<j<<": "<<count<<endl;
	}
};

int ca::ia=0;
int ca::jb=0;
int ca::andS[1000][1000];

int main() {
	//cout << "QB" << endl; // prints QB

	ifstream ifile;
	ifile.open("B-small-attempt0.in");
	ofstream ofile;
	ofile.open("output.txt");
	int n;
	ifile>>n;
	//cout<<n<<"yi"<<endl;
	for (int i=1;i<=n;i++)
	{
		ca c1(ifile,ofile,i);
	}
	ifile.close();
	ofile.close();
	return 0;
}
