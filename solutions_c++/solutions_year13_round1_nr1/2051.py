//2013 GCJ Qualification round A. Tic-Tac-Toe-Tomek

#include <iostream>
#include <string>
#include <fstream>
#include <math.h>

using namespace std;
//const double PI = 4.0*atan(1.0);
double check(double r, double t)
{
	double y=1;
	double sum=0;
	

	while (sum<t)
	
	{
		sum+=(2*r-3+4*y);
	    cout<<sum<<endl;
		y++;
	}
	cout<<y<<endl;
	if (sum>t)
		
		y=y-2;
	else
		y=y-1;

	return y;

}

int main()
{
	//ifstream fin("a.in");
	ifstream fin("A-small-attempt0.in");
	//ifstream fin("A-large.in");
	int T;
	fin>>T;
	//ofstream fout("a.out");
	ofstream fout("A-small-attempt0.out");
	//ofstream fout("A-large.out");	
		
	
	//char **s = new char*[4];
	
	
	

		for (int n=1;n<=T;n++)
	{
		
		//char* A=new char[4];
		//char* B=new char[4];

		double r;
		double t;
		fin>>r>>t;
		
			
			
		double y=check(r,t);
		int y1=double(y);
	    	
		fout<<"Case #"<<n<<": ";
	
		fout<<y1<<endl;

		//delete []A;
	   // delete []B;
		
	}
	
	
		
	return 0;
}