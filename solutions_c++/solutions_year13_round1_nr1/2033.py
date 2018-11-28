/*
ID: benjamin.chen@aztopia.com
PROG: 2013 1A Problem A: 
LANG: C++
*/

#include <fstream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <limits>

using namespace std;

int main()
{
	ifstream fin("A_input.in");
	int T;
	fin>>T;
	cout<<"T: "<<T<<endl;
	ofstream fout("A_output.out");

	for(int i=0;i<T;i++)
	{
		unsigned long long int r,t;//r: starting circle radius, t: mL of paint (1 mL => pi cm^2)
		fin>>r>>t;
		cout<<"r: "<<r<<endl;
		cout<<"t: "<<t<<endl;
		long double l = sqrt((.5*r-.25)*(.5*r-.25) + .5*t);
		unsigned long long int m = floor(l - .5*r + .25);

		//Treat m as approximation
		unsigned long long int s = m+15;
		while((2*r+2*s-1)*s > t)
		{
			s--;
		}

		fout<<"Case #"<<(i+1)<<": "<<s<<endl;
		cout<<"Case #"<<(i+1)<<": "<<s<<endl;
	}

	return 0;
}
