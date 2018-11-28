/* 
 * File:   Lawnmower.cpp
 * Author: pablo
 *
 * Created on April 12, 2013, 10:55 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <sstream>

typedef std::vector< std::vector<int> >  TLawn;

bool verifyLawn( TLawn& );
int possibleOut( TLawn&, int, int );
bool row( TLawn& lawn, int , int  );
bool column( TLawn& lawn, int, int );

int N, M;

int main()
{
    int n;
    std::string caseW = "Case #";
    std::string caseP = ": ";
    std::string yes = "YES";
    std::string no = "NO";

    std::cin >> n;
       
    for( int c=1; c <= n; c++ )
    {      
       std::cin >> N >> M;
       
       TLawn lawn( N );
        
       int num;
       for( int i=0; i < N; i++ )
       {
           for( int j=0; j < M; j++ )
           {
               std::cin >> num;
               lawn[i].push_back( num );               
           }
       }
       
       if( N == 1 || M == 1 )
       {
           std::cout << caseW << c << caseP << yes << std::endl;
       }else{
           
           bool possible = verifyLawn( lawn );           
           if( possible )
               std::cout << caseW << c << caseP << yes << std::endl;
           else
               std::cout << caseW << c << caseP << no << std::endl;
           
       }                            
        
    }


  return( 0 );
}



bool
verifyLawn( TLawn& lawn )
{
    int minF = 0;
    int minC = 0;
    int maxF = N-1;
    int maxC = M-1;
    
    int maximun = 2;
    
    
    for( int i=0; i < N; i++ )
    {
        for( int j=0; j < M; j++ )
        {
            if( lawn[i][j] != maximun )
            {
                if( !column( lawn, i, j ) && !row( lawn, i , j))
                    return( false );
            }                        
        }
        
    }
    
    
    
    
    /*
    
    // ===============================
    //         lawn internal values
    // ===============================
    for( int i=1; i < N-1; i++ )
    {
        for( int j=1; j < M-1; j++ )
        {
            int value = possibleOut( lawn, i, j );             
            if( value == 3)        
            {
                if( ( lawn[i][j] == lawn[i][j-1] && lawn[i][j] == lawn[i][j+1] ) || ( lawn[i][j] == lawn[i-1][j] && lawn[i][j] == lawn[i+1][j] ) )                                    
                    continue;                
                else
                    return( false );
            }
            else if( value == 2 )
            {
                if ( lawn[i][j] == lawn[i-1][j] && lawn[i][j] == lawn[i+1][j] )
                    continue;
                else
                    return( false );                
            }
            else if( value == 1 )
            {
                if( lawn[i][j] == lawn[i][j-1] && lawn[i][j] == lawn[i][j+1] )
                    continue;
                else
                    return( false );                
            }else                
                return( false );
        }
    }
    
     * 
     * 
    
    
    // ===============================
    //         lawn external values
    // ===============================
    
    std::cout << "Internos validos!" << std::endl;
    
    for( int j=0; j < M; j++ )
    {
        if( lawn[0][j] != maximun )
        {
            if( !column( lawn, j ) && !row( lawn, 0) )
                return( false );                
        }
    }
    
    std::cout << "Fila cero valida!" << std::endl;
    
    for( int j=0; j < M; j++ )
    {
        if( lawn[N-1][j] != maximun )
        {
            if( !column( lawn, j ) && !row( lawn, N-1) )
                return( false );                
        }
    }
    
    std::cout << "Fila final valida!" << std::endl;
    
    for( int i=0; i < N; i++ )
    {
        if( lawn[i][0] != maximun )
        {
            if( !column( lawn, 0 ) && !row( lawn, i) )
                return( false );                
        }
    }
    
    std::cout << "Col cero valida!" << std::endl;
    
    for( int i=0; i < N; i++ )
    {
        if( lawn[i][M-1] != maximun )
        {
            if( !column( lawn, M-1 ) && !row( lawn, i ) )
                return( false );                
        }
    }
    
    std::cout << "Col final valida!" << std::endl;
    
     * 
     */
    
    
    return( true );
     
}


int 
possibleOut( TLawn& lawn, int i, int j )
{
    // Salida Ambas = 3
    // Salida Vertical = 1
    // Salida Horizontal = 2
    // Sin Salida = 0
    
    int minF = 0;
    int minC = 0;
    int maxF = N-1;
    int maxC = M-1;
    
    int poss = 0;
    
    if( ( lawn[i][j] == lawn[minF][j] && lawn[i][j] == lawn[maxF][j] ) )
    {
        poss++;
    }
           
    if( lawn[i][j] == lawn[i][minC] && lawn[i][j] == lawn[i][maxC] )
    {
        poss += 2; 
    }
    
    return( poss );
}


bool
column( TLawn& lawn, int i, int j )
{
    int value = lawn[i][j];   
    
    for( int x = 0; x < N; x++ )
    {        
        if( lawn[x][j] != value )
            return( false );
    }        
    
    return( true );
}

bool
row( TLawn& lawn, int i, int j )
{
    int value = lawn[i][j];
    
    for( int x = 0; x < M; x++ )
    {
        if( lawn[i][x] != value )
            return( false );
    }                   
    
    return( true );
}
