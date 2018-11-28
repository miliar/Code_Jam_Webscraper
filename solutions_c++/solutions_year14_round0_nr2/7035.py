#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

int main()
{
	ifstream infile;
	infile.open("input.txt"); //the input file name here
	ofstream ofile;
	ofile.open("answer.txt");
	int t;
	infile>>t;
	for(int i=1;i<t+1;i++)
	{
		double x,f,c;
		infile>>c>>f>>x;

		int n=1;
		double t0,t1,t2,y=0;
		
		
		t0=x/2;
		y=1/((n-1)*f+2);
		t1= c*y + x/(n*f+2);
		n++;
		y= y + 1/((n-1)*f+2);
		t2= c*y+x/(n*f+2);

		while(t2<t1)
		{
			t1=t2;
			n++;
			y= y + 1/((n-1)*f+2);
			t2=c*y+x/(n*f+2);
		}
		 ofile<<fixed;
         ofile << setprecision(7);
		if(t1<t0) 
			ofile<<"Case #"<<i<<": "<<t1<<endl;
		else
			ofile<<"Case #"<<i<<": "<<t0<<endl;

		
	}



	
	return 0;
}

