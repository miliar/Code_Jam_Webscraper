#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	ifstream myfile;
	myfile.open(argv[1]);
    int num_test;
	myfile>>num_test;
	
	for (int num=0;num<num_test;num++)
	{
		double C;
		double F;
		double X;
		double r=2;
		double t=0;
		myfile>>C;
		myfile>>F;
		myfile>>X;

		while(X/r > (C/r + X/(r+F)))
		{
          t+=C/r;
          r+=F; 
		}
		t+=X/(r);
		cout.precision(20);
		cout<<"Case #"<<num+1<<": "<<t<<endl;
		string a;
		getline(myfile, a);
	}
}
