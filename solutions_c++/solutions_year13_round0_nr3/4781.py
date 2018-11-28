#include <iostream>
#include <cstdlib>
#include <vector>
#include <sstream>


typedef std::vector<bool>  TSquare;
typedef std::vector<int>  TRoot;

void fillSquaresAndRoots( TSquare& , TRoot& );
bool palindrome( int );

int main()
{

    int n;
    std::string caseW = "Case #";
    std::string caseP = ": ";

    std::cin >> n;


    TSquare squares( 1025, false );
    TRoot roots( 1000, 0 );
    
    fillSquaresAndRoots( squares, roots );

    for( int c=1; c <= n; c++ )
    {
        int A,B;
        std::cin >> A >> B;
        int cont = 0;

        for( int i=A; i<=B; i++ )
        {                       
            if( squares[i] && palindrome( i ) && palindrome( roots[i] ) )            
                  cont++;
            
        }

        std::cout << caseW << c << caseP << cont << std::endl;
    }


  return( 0 );
}

void
fillSquaresAndRoots( TSquare& squares, TRoot& roots )
{
    int i=0;
    while( i*i < 1000 )
    {
        squares[i*i] = true;
        roots[i*i] = i;
        i++;
    }

}

bool palindrome( int num )
{
    std::stringstream ss;
    ss << num;
    std::string n = ss.str();

    for( int i=0; i < n.size()/2; i++ )
    {
        if( n[i] != n[n.size()-i-1] )
        {
            return( false );
        }
    }

    return( true );

}
