#include<fstream>
#include <string>
#include <sstream>
#include<iomanip>
#include<iostream>
#include<iostream>
using namespace std;
int main()
{
	ofstream myout;
	myout.open("output.txt",ios::out);
	int tst;
	cin>>tst;
	for(int u=0;u<tst;u++)
	{
	
	double c,f,x;
	cin>>c>>f>>x;
	double r=2;
	double time=0;
	if(c<x)
	{
		
		l1:time+=c/r;
		if(((x-c)/r)>=(x/(r+f)))
		{
			
			r=r+f;
		
			goto l1;
		}
		else time+=(x-c)/r;
	}
	else {
		time=x/2;
	}
	myout<<"Case #"<<u+1<<": "<<setiosflags(ios::fixed) << setprecision(7) << time << endl;

	
	}
	return 0;
}
