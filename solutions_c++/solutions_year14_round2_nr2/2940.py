#include<iostream>
#include<fstream>
using namespace std;

unsigned long long find ( unsigned long long a, unsigned long long b, unsigned long long k )
{
	if ( a>b )
	{
		unsigned long long temp =a;
		a=b;
		b=temp;
	}
	unsigned long long count=0;
	for ( unsigned long long i=0 ; i< a ; ++i )
	{
		for ( unsigned long long j=0 ; j<b ; j++)
		{
			if ( (i&j) < k )
				++count;
		}
	}
	return count;
}

int main ()
{
	ifstream input ( "B-small-attempt0.in");
	int x;
	input>>x;
	unsigned long long** cases;
	cases = new unsigned long long* [x];
	for ( int i=0;i<x;i++)
		cases[i] = new unsigned long long[3];

	for  ( int i=0 ; i<x; i++)
		for ( int j=0 ; j<3;j++ )
			input>>cases[i][j];
	
	ofstream output ("lottery.out");

	for ( int i=0 ; i<x ; i++ )
		output<<"Case #"<<i+1<<": "<< find ( cases[i][0] , cases[i][1] , cases[i][2])<<endl;

		


	return 0;
}
