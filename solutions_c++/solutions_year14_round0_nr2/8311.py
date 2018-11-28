#include <fstream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <cmath>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("output.txt");

int main()
{

	int t,i,j;

	double c,x,f;

	cin>>t;

	for(i=0; i<t; ++i)
	{
		cin>>c>>f>>x;

		long double res = x/2; 
		long double t0 = c/2;
		double y = 2;



		while(t0 + x/(f+y) < res)
		{
			res = t0 + x/(f+y) ;
			y += f;
			t0 += c/(y);	

		
		}

		cout<<"Case #"<<i+1<<": ";
		cout<<setiosflags(ios::fixed | ios::showpoint)<< setprecision(7)<<res<<endl;
	}

	return 0;
}