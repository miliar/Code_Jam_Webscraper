#include<fstream>
#include<conio.h>

using namespace std ;
ifstream fin ;
ofstream fout ;

int main()
{
	int T, A, B, K, i, j, count=0, c=1 ;

	fin.open ( "B-small-attempt1.in.txt", ios::in ) ;
	fout.open ( "output.txt", ios::out|ios::trunc ) ;

	fin >> T ;

	while (T--)
	{
		fin >> A >> B >> K ;
		count = 0 ;
		for ( i=0 ; i<A ; i++ )
			for ( j=0 ; j<B ; j++ )
				if ( (i&j) < K )
					count++ ;

		fout << "Case #" << c++ << ": " << count << endl ;
	}
	return 0 ;
}