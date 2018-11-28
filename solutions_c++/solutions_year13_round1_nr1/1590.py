#include<iostream>
#include<fstream>
#include<math.h>
#include<fstream>
using namespace std;
int getRings(long long r,long long t);
int main()
{
	int n,i=0,*out;
	ofstream f("out.txt");
	long long r,t;
	cin>>n;
	out=new int[n];
	while(i<n)
	{
		cin>>r>>t;
		out[i]=getRings(r,t);
		i++;
	}

	for(i=0;i<n;i++)
	{
		f<<"Case #"<<(i+1)<<": "<<out[i]<<"\n";
	}
	delete [] out;
	return 0;
}

int getRings(long long r,long long t)
{
	long long ri=r;
	long long paint=0;
	int rings_n=0;
	while(paint<=t)
	{
		paint+=(2*ri+1);
		if(paint<=t)
		{
			rings_n++;
			ri+=2;
		}
	}
	return rings_n;
}
