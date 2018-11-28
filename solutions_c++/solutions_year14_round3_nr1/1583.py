#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <Windows.h>

using namespace std;
int total=0;
void abc(long long int p,long long int q,int & total)
{
	++total;
	if(total>40)
		return;
	if(2*p-q<=q && 2*p-q>=0)
	{
		int c=total;
		if((2*p-q==0 || 2*p-q==1))// && q==1)
			return;
		else
		{
			abc(2*p-q,q,c);
			if(c<=40)
				return;
		}
	}
	abc(2*p,q,total);
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("my.out");
	int t;
	char temp;
	long long int p;
	long long int q;
	int total=0;
	fin>>t;
	for(int i=0;i<t;++i)
	{
		total=0;
		fin>>p>>temp>>q;
		abc(p,q,total);
		if(total<40 && q%2==0)
			fout<<"Case #"<<i+1<<": "<<total<<endl;
		else
			fout<<"Case #"<<i+1<<": impossible"<<endl;
	}
	fin.close();
	fout.close();

	return 0;
}