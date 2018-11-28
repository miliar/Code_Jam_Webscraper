#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
using namespace std;

double c, f, x;
double czas, s;

bool opyla_sie()
{
	return c/s+x/(s+f)<x/s;
}

vector <double> res;

int main()
{
	int t; cin>>t;
	for(int k=1; k<=t; k++)
	{
		cin>>c>>f>>x;
		czas=0;
		s=2;
		while(opyla_sie()) {czas+=c/s; s+=f;}
		czas+=x/s;
		res.push_back(czas);
	}
	for(int i=0; i<res.size(); i++) printf("Case #%d: %.7lf\n",i+1,res[i]);
	return 0;
}

