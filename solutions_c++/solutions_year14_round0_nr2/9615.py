#include <iostream>
#include <fstream>
#include <process.h>
#include <iomanip>
using namespace std;
double icookie[101][4];
int nc;	// nc=no. of cases
double r,tc;	// r= rate of cookies in 1 seconds, tc=total cookies
double caltime(int);

double caltime(int i)
{
	double tt,rt;	// total time,required time to buy a farm
	double c,f,x;
	c=icookie[i][1];
	f=icookie[i][2];
	x=icookie[i][3];
	rt=c/r;	// c/r
	tc=tc+c;
	if((x-tc)/r>(x-(tc-c))/(r+f)) 
	{
		tc=tc-c;
		r=r+f;
		tt=rt+caltime(i);
		return tt;
	}
	else
	if((x-tc)/r<=(x-(tc-c))/(r+f))
	{
		double temp=(x-tc)/r;	//time required to create remaining cookies
		
		temp=rt+temp;
		return temp;
	}
}
int main()
{		
	int i,j;	
	double ts;	//ts=total no of seconds
	ifstream inf;
	ofstream outf;
	outf.open("outfile.txt");
	inf.open("B-small-attempt0.in");
	if(!inf)
	{
		cerr << "error in opening file" << endl;
        exit(1);
	}
	inf>>nc;
	for(i=1;i<=nc;i++)
	{
		for(j=1;j<=3;j++)
		{
			inf>>icookie[i][j];
		}
	}
	for(i=1;i<=nc;i++)
	{	
		tc=0;
		r=2;	
		ts=caltime(i);
	
		outf<<fixed<<setprecision(7)<<"Case #"<<i<<": "<<ts<<endl;	
	}
	inf.close();
	system("pause");		
	return 0;
}

