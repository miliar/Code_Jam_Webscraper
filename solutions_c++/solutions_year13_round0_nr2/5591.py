#include<iostream>
#include<vector>
#include<cstdlib>
#include <cstdio>
#include<cstring>
#include<cmath>
#include<math.h>
#include<sstream>
#define SS stringstream
#define SZ(S) S.size()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std ;
int main ()
{
    READ("B-small-attempt3.in");    // esm l downloaded file ay 7aga
    WRITE("B-small-attempt3.out");  // esm l output file w dah hn3melo upload m3 l source pp



    int t , n , m;
    cin >> t ;

    for(int k=1 ; k <= t ; k++)
    {
        cin >> n >> m ;

        char **grid = new char *[n] ;
        char **check = new char *[n] ;
        for(int i=0 ; i<n ; i++)
        {
            grid[i] = new char [m] ;
            check[i] = new char [m] ;
            for(int j=0 ; j<m ; j++)
            {
                cin >> grid[i][j] ;
                check[i][j] = '2' ;
            }
        }

        // ->
        bool b = 1 ;
        for(int i=0 ; i<n ; i++)
        {

            b = 1 ;
            for(int j=0 ; j<m ; j++)
            {
                if( grid[i][j] == '2' )
                {
                    b = 0 ;
                    break ;
                }
            }
            if( b == 0 )
                continue ;

            for(int j=0 ; j<m ; j++)
                check[i][j] = '1' ;
        }


        // \/
        for(int i=0 ; i<m ; i++)
        {

            b = 1 ;
            for(int j=0 ; j<n ; j++)
            {
                if( grid[j][i] == '2' )
                {
                    b = 0 ;
                    break ;
                }
            }
            if( b == 0 )
                continue ;

            for(int j=0 ; j<n ; j++)
                check[j][i] = '1' ;
        }



        for(int i=0 ; i<n ; i++)
        {
            b = 1 ;
            for(int j=0 ; j<m ; j++)
            {
                if( check[i][j] != grid[i][j] )
                {
                    b = 0 ;
                    break ;
                }
            }
            if( b == 0 )
                break;
        }
        for(int i= 0 ; i = 0 ; i++)
        {
            for(int j=0 ; j<m ; j++)
            {
                if( check[i][j] != grid[i][j] )
                {
                    b = 0 ;
                    break;
                }

            if( b == 0 )
                break;
            }
        }

    cout << "Case #" << k << ": " ;
    if( b == 1 )
        cout << "YES\n";
    else
        cout << "NO\n";
        }



return 0;
}




/*
#include<iostream>
#include<vector>
#include<cstdlib>
#include <cstdio>
#include<cstring>
#include<cmath>
#include<math.h>
#include<sstream>
#define SS stringstream
#define SZ(S) S.size()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std ;
bool check(int num)
{
    SS ss ;
    ss << num ;

    string S ;
    ss >> S ;

    for(int i=0 , j=SZ(S)-1 ; i<SZ(S) ; i++,j--)
    {
        if( S[i] != S[j] )
            return 0 ;
    }
    return 1 ;
}
int main ()
{
//    long double x = 1213326733121 ;
//    cout << x ;

//    cout << (long double) sqrt (  x);


//    READ("C-small-attempt0.in");    // esm l downloaded file ay 7aga
//    WRITE("C-small-attempt0.out");  // esm l output file w dah hn3melo upload m3 l source pp

    int t , c ;
    unsigned long long  n , m ;
    cin >> t ;

    string S , T ;
    for(int k=1 ; k<=t ; k++)
    {
        cin >> n >> m ;

//        while( n % 10 == 0 )
//            n /= 10 ;
//
//        while( m % 10 == 0 )
//            m /= 10 ;

//        cout << n << " " << m << endl ;

        long double sq ;
        bool b = 1 ;
        c = 0 ;
        for(int i=n ; i <= m ; i++)
        {
            cout << i << "\n" ;
            b = check(i) ;
            if( b == 0 )
               continue ;

            sq = sqrt(i) ;
            if( sq != floor(sq) )
                continue ;

            b = check( sq ) ;
            if( b == 1 )
                c++ ;

         //   cout << i << "\n" ;


        }
        cout << "Case #" << k<< ": " << c << endl ;
    }


    return 0 ;

}
*/
/*
#include<iostream>
#include<vector>
#include<cstdlib>
#include <cstdio>
#include<cstring>
#define SZ(S) S.size()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std ;
int check(vector<string>S)
{
    int cX = 0 , cO = 0 , cdot = 0 , cT = 0 ;
    bool b = 1 ;
    // 1st ofoki
    for(int i=0 ; i<4 ; i++)
    {
        cX = cO = cdot = cT = 0 ;
        for(int j=0 ; j<4 ; j++)
        {
            if( S[i][j] == 'X' )
                cX++;
            else if( S[i][j] == 'O' )
                cO++;
            else if( S[i][j] == 'T' )
                cT++;
        }
        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;

    if( cT + cX + cO <  4 )
       b = 0 ;
    }

    for(int j=0 ; j<4 ; j++)
    {
        cX = cO = cdot = cT = 0 ;
        for(int i=0 ; i<4 ; i++)
        {
            if( S[i][j] == 'X' )
                cX++;
            else if( S[i][j] == 'O' )
                cO++;
            else if( S[i][j] == 'T' )
                cT++;
        }
        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }

    cT = cX = cO = 0;
    for(int i=0 ; i<4 ; i++)
    {
        if( S[i][i] == 'X' )
            cX++;
        else if( S[i][i] == 'O' )
            cO++;
        else if( S[i][i] == 'T' )
            cT++;

//        cout << cT << " " << cO << " " << cX << endl ;

        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }
//    cout << " ? " ;

    cT = cX = cO = 0;
    for(int i=0 ; i<4 ; i++)
    {

        if( S[i][3-i] == 'X' )
            cX++;
        else if( S[i][3-i] == 'O' )
            cO++;
        else if( S[i][3-i] == 'T' )
            cT++;

        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }

    if( b == 1 )
        return 3 ;
    return 4;

}
int main ()
{
    // Case #1
    READ("A-large.in");    // esm l downloaded file ay 7aga
    WRITE("A-large.out");  // esm l output file w dah hn3melo upload m3 l source pp

    int t ;
    cin >> t ;

    for(int k=1 ; k<=t ; k++)
    {
        vector<string>grid(4,"....");

        cin >> grid[0] >> grid[1] >> grid[2] >> grid[3] ;

        int res = check(grid) ;

        cout << "Case #" << k << ": " ;

        if( res == 1 )
           cout << 'X'<< " won\n";
        else if( res == 2 )
           cout << 'O'<< " won\n";
        else if( res == 3 )
           cout << "Draw\n";
        else
           cout << "Game has not completed\n";


    }

    return 0 ;
}*/

//freopen("in.txt", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
//freopen("out.txt", "wt", stdout); // same for out.txt
/*
#include<algorithm>
#include<iostream>
#include<vector>
#include<cmath>
#define SZ(S) S.size()
using namespace std;
int main ()
{
    int n , m , mini , counter ,ind ;
    cin >> n >> m ;

    vector<int>vec(m,0) , far2(m,0) ;
    for(int i=0 ; i<n ; i++)
    {
        mini = 1000000 , counter = 1 ;

        for(int j=0 ; j<m ; j++)
        {
            if( mini > vec[j] )
            {
                counter = 1 ;
                mini = vec[j] ;
                ind = j ;
            }
            else if( mini == vec[j] )
                counter++;


            far2[j] = abs( (m+1)/2 - j -1 );
        }
  //      cout << "?" ;

//        for(int k = 0 ; k < m ; k++)
//            cout << far2[k] << " " ;
//        cout << endl ;


        if( counter > 1 )
//        {
//            vec[ind]++;
//            cout << ind + 1 ;
//        }
//        else
        {
            int min = *min_element( far2.begin() , far2.end() ) ;



            for(int j=(m+1)/2 , k=(SZ(vec)+1)/2 -1; k>=0 ; j++,k--){
                    cout << k << " " << j << endl ;
                if( vec[k] <= vec[j] && vec[k] == min )
                    ind = k ;
                else if( vec[k] > vec[j] && vec[j] == min )
                    ind = j ;
            }
        }
        cout << "---------\n";

        vec[ind]++;
   //     cout << ind + 1 << endl ;
    }

    return 0 ;
}*/
