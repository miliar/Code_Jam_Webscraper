#include<iostream>
#include<fstream>
using namespace std ;

int arrange( char str[] )
{
	int count = 0 , ln = 0 ;
	for( int i=0 ; str[i] != '\0' ; i++ , ln ++ ) ;
	for( int i=ln-1 ; i>=0 ; i-- )
	{
		if( str[i] == '-')
		{
			for( int j=i ; j>=0 ; j-- )
			{
				if( str[j] == '-')
					str[j] = '+' ;
				else 
					str[j] = '-' ;
			}
			count += 1 ;
		}
	}
	return count ;
}

int main()
{
	ifstream infile ;
	infile.open("B-large.in", ios :: in) ;
	ofstream outfile ;
	outfile.open( "outputBlarge.txt", ios :: out) ; 
	int T ;
	char str[200] ;
	infile >> T ;
	infile.seekg(sizeof(int)) ;
	for( int i=0 ; i<T ; i++)
	{
		infile.getline( str ,200,'\n') ;
		outfile<<"Case #"<<i+1<<": ";
		outfile<<( arrange(str) ) << "\n" ;
	}
	return 0 ;
}
