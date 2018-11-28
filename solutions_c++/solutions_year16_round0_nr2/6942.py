#include <iostream>
#include <string>
#include <fstream>
using namespace std ;
int dizi[100000],result[10000] ;
int rest(int uzunluk)
{
	int x=0,y=1 ;
	int syc = 0 ;
	for (int i = 1; i <= uzunluk; ++i)
	{
		if( dizi[i] == x && dizi[i-1] == y)
		{
			syc++ ;
			x=(x+1)%2 ;
			y=(y+1)%2 ;
		}
	}
	return syc ;
}
int main()
{
	ifstream dosya("girdi.txt") ;
	ofstream cikti("cikti.txt") ;
	int n ;
	string str ;
	dosya >> n ;
	for (int i = 1; i <= n; ++i)
	{
		dosya >> str ;
		int uzunluk=str.length() ;
		fill(&dizi[0],&dizi[10000],-1) ;

		for (int j = 0; j < uzunluk; ++j)
		{
			if( str[j]=='+' )
				dizi[uzunluk-j] = 1 ;
			else
				dizi[uzunluk-j] = 0 ;
		}

		dizi[0] = 1 ;
		result[i] = rest(uzunluk) ;
		
	}


	for (int i = 1; i <= n ; ++i)
	{
		cikti << "Case #" << i << ": " << result[i] << endl  ;
	}

}