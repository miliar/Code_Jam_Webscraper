#include <iostream>
#include <fstream>
#include <cmath>
#include <cstring>
#include <climits>

int getMinHeight ( char **grid , int N , int M ) {

    int i , j;

    int minHeight=INT_MAX;

    for ( i = 0 ; i < N ; ++i ) {

        for ( j = 0 ; j < M ; ++j ) {

            if ( grid[i][j]-'0' < minHeight )
                minHeight = grid[i][j]-'0';
        }
    }

    return minHeight;
}

bool line ( char **grid , int i , int minHeight , int M ) {

    int j;

    int n ( 0 );

    for ( j = 0 ; j < M ; ++j ) {

        n+=grid[i][j]-'0';
    }

    if ( n == M*minHeight )
        return true;

    return false;
}

bool col ( char **grid , int j , int minHeight , int N ) {

    int i;

    int n ( 0 );

    for ( i = 0 ; i < N ; ++i ) {

        n+=grid[i][j]-'0';
    }

    if ( n == N * minHeight )
        return true;

    return false;
}

bool check ( char **grid , int N , int M ) {

    int i , j;

    int minHeight = getMinHeight ( grid , N , M );

    for ( i = 0 ; i < N ; ++i ) {

        for ( j = 0 ; j < M ; ++j ) {

            if ( grid[i][j]-'0' == minHeight ) {

                if ( !line ( grid , i , minHeight , M ) && !col ( grid , j , minHeight , N ) ) {

                    return false;
                }
            }
        }
    }

    return true;
}

int main ( int argc , char *argv[] ) {

    std::ifstream input ( "input.txt" );
    std::ofstream output ( "output.txt" );
    if ( !input ) std::cout << "failed to open file." << std::endl;
    else {

        char **grid;
        int i , j , n , N , M;

        input >> n;

        for ( i = 0 ; i < n ; ++i ) {

            input >> N >> M;

            grid = new char*[N];
            for ( j = 0 ; j < N ; ++j )
                grid[j] = new char[M];

            j = 0;

            while ( j < N*M ) {

                input >> grid[j/M][j%M];
                j++;
            }

            bool state = check ( grid , N , M );

            output << "Case #" << i+1 << ": ";
            if ( state ) output << "YES";
            if ( !state ) output << "NO";
            output << std::endl;
        }
    }

    return 0;
}
