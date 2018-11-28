#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
#include<math.h>
using namespace std;

ofstream op;

int main()
{
	ifstream ip;
	ofstream op;
	unsigned long i,j,k,l;
	unsigned long T,r,t,n;
	op.open("output.txt");	
	ip.open("A-small-attempt2.in");
	ip>>T;
	double low,high,mid;
	double lown,highn,midn;
	
	
	int temp;
	for(l=0;l<T;l++)
	{
		ip>>r>>t;
		low=(r+1)*(r+1);
		low=low-r*r;
		high=low;
		midn=1;
		for(midn=1;high<t;midn++)
		{
			low=low+4;
			high=high+low;
		}
		if(high>t)
			midn--;
		//cout<<l<<"\t"<<lown<<"\t"<<highn<<"\n";
		op<<"Case #"<<l+1<<": "<<(unsigned long)midn<<"\n";
		
	}
	ip.close();
	op.close();
	return 0;
	
}
