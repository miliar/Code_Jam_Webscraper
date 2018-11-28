#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;

unsigned long long root(unsigned long long a, unsigned long long b, unsigned long long c)
{
	if(b*b-(4*a*c)<0)
		return 0;

	//cout << sqrt(b*b-4*a*c) << endl;
	//cout << ((-1*b)+(int)sqrt(b*b-4*a*c)) << endl << (2*a) << endl;
	return ((-1*b)+(unsigned long long)sqrt(b*b-4*a*c))/(2*a);
}

void solve(unsigned long long r, unsigned long long t)
{
	out << root(2, 2*r-1, -1*t) << endl;
}

int main()
{
	int T,n;
	unsigned long long int r,t;
	in.open("A-small-attempt0.in");
	out.open("output.txt");
	in >> T;
	n=T;
	while(T-- > 0)
	{
		out << "Case #"<< (n-T) << ": ";
		in >> r >> t;
		solve(r, t);
	}
	return 0;
}
