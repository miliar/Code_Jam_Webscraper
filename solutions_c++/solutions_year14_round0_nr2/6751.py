#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

long double  determine ( long double cost , long double farm , long double win )
{
	long double rate=2;
	int flag=1;
	long double time=cost/rate;
	while ( flag )
	{
		if ( (win - cost)/rate > (win)/(rate+farm) )
		{
			rate += farm;
			time += cost/rate;
		}

		else
		{
			
			flag--;
			time+= (win-cost)/rate;
		}
	}

	return time;
}

int main()
{
	int caseX;
  ifstream input ("B-large.in");
	ofstream output("Cookie.out");
	input >>caseX;
	long double** cases = new long double* [caseX];
	for ( int i=0 ; i<caseX ; i++ )
		cases[i] = new long double [3]; 
  for ( int i=0 ; i<caseX ; i++ )
		for ( int j=0 ; j<3 ; j++ )
			input>>cases[i][j];
	for ( int i=0 ; i<caseX ; i++)
	{
		output.precision(7);
		output.setf( ios::fixed , ios::floatfield);
		long double temp = determine ( cases[i][0] , cases [i][1] , cases[i][2] );
		output<<"Case #"<<i+1<<": "<<temp;
		output<<endl;
	}

  return 0;
}
