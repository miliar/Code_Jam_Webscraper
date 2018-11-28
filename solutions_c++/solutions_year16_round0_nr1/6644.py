#include<iostream>
#include<fstream>
using namespace std ;

int count_sheep( int n )
{
	int arr[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 } ;
	int count = 0 , num = n , duplicate , digit , counter = 1 ;
	if( n == 0 )
		return -1 ;
	while( count != 10 )
	{
		duplicate = num ;
		counter += 1 ;
		while( duplicate != 0 )
		{
			digit = duplicate % 10 ;
			duplicate = duplicate / 10 ;
			for( int i=0 ; i<10 ; i++ )
				if( digit == i )
					arr[i] = 1 ;
		}
		for( int j=0 ; j<10 ; j++ )
			if( arr[j] != 0 )
				count +=1 ;
		if( count == 10 )
				break ;
		else
			count = 0 ;
		num = n * counter ;	
	}
	return num ;
}

int main()
{
	ifstream infile ;
	infile.open("A-large.in", ios :: in) ;
	ofstream outfile ;
	outfile.open( "outputlarge.txt", ios :: out) ;
	int T , number ;
	infile >> T ;
	for( int i=0 ; i<T ; i++)
	{
		infile >> number ;
		outfile<<"Case #"<<i+1<<": ";
		if( count_sheep(number) == -1 )
			outfile<<"INSOMNIA\n";
		else
			outfile<<( count_sheep(number) ) << "\n" ;
	}
	return 0 ;
}
