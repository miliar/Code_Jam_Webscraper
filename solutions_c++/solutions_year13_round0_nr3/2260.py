#include<fstream>
#include<iostream>
#include<math.h>

using namespace std;

int palin(long long int x)
{
	long long int y=0,c=x;;
	while(x!=0)
	{
		y*=10;
		y+=x%10;
		x/=10;
	}
	return c==y;
}

int main()
{
	int t,tc,c;
	long long int x,a,b,i,j;
	ifstream ifile("D:/in.in");
	ofstream ofile("D:/out.txt");
	ifile>>t;
	for(tc=0;tc<t;++tc)
	{
		c=0;
		ifile>>a>>b;
		i=sqrt(a);
		if(i*i<a) ++i;
		j=sqrt(b);
		for(x=i;x<=j;++x)
		if(palin(x))
		{	
			if(palin(x*x)) ++c;
		}
		ofile<<"Case #"<<tc+1<<": "<<c<<endl;
	}
	return 0;
}
