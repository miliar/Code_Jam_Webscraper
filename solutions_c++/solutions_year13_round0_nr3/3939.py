#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>

using namespace std;

bool is_perfect_sq( double );
double get_quotient( double, double );
bool is_palindrome( double );

int main()
{
	ifstream infl( "C-small-attempt0.in" );
	ofstream outfl( "fair_and_square_small.txt" );
	
	int num_of_tests;
	double start;
	double end;

	double num;
	
	int case_num = 0;

	infl >> num_of_tests;

	while( case_num < num_of_tests )
	{
		infl >> start;
		infl >> end;

		num = start;

		double total = 0;

		while( num <= end )
		{
			if( is_palindrome( num ) && is_perfect_sq( num ) && is_palindrome( sqrt( num )))
			{  total++; }

			num++;
		}

		case_num++;

		outfl << "Case #" << case_num << ": "  << total << endl; 
	}
}


bool is_perfect_sq( double num )
{
	double sqrt_of_num = sqrt( num );

	if(( fmod( sqrt_of_num, 1 ) == 0 ))
	{  return true; }
	else
	{  return false;  }
}

double get_quotient( double num, double divider )
{  return ( num - fmod( num, divider )) / divider;  }

bool is_palindrome( double num )
{
	double divider = 1;
		
	while( get_quotient( num, divider ) >= 10) 
	{  divider *= 10;  }       

	while( num != 0 ) 
	{
		double left = get_quotient( num, divider );
		double right = fmod( num, 10 );

		if( left != right ) 
		{  return false;  }

		num = get_quotient( fmod( num, divider ), 10 );
		divider = get_quotient( divider, 100 );
	}
	
	return true;
}
