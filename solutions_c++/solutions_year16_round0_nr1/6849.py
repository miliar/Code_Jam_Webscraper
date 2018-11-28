#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std ;
int testcase[10000],n ;
int dizi[1000],tut ;
int result( int m ,int syc ) 
{
	int r = m ;
	if(syc == 100000)
		return -1 ;
	
	int w=0 ;
	for( int i=9 ; i>=1 ; )
	{
		i-- ;
		int y = pow(10,i) ;
		if(w || m/y)
		{
		 
			dizi[m/y]++ ;
			m%=y ;
			w=1 ;
		}
	} 

	int x = 0 ;
	for (int i = 0; i <= 9; ++i)
		if(dizi[i])
			x++ ;

	if( x == 10 )
		return r ;
	else
		return result( tut*(syc+1) , syc+1 ) ;
}
int main()
{
	ifstream dosya("girdi.txt") ;
	ofstream cikti("cikti.txt") ;
	dosya >> n ;
	for (int i = 1; i <= n; ++i)
		dosya >> testcase[i] ;
	
	int cvp ;

	for (int i = 1; i <= n ; ++i)
	{
		fill(&dizi[0],&dizi[15],0) ;
		
		tut=testcase[i] ;
		
		cikti << "Case #" << i << ": " ;
		
		cvp = result(testcase[i],1) ;

		if( cvp == -1 )
			cikti << "INSOMNIA " << endl ;
		else
			cikti << cvp << endl ;
	}
}