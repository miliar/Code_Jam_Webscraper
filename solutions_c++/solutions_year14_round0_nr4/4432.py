#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std ;

const int NMAX = 15 ;

ifstream cin("war.in") ;
ofstream cout("war.out") ;

inline int max (int a, int b)
{
    if(a > b) return a ;
    else return b ;
}
inline int min (int a, int b)
{
    if(a > b) return b ;
    else return a ;
}

int T, N;
double A[NMAX], B[NMAX];
int d = 0 ;
int X, Y ;

int main()
{

    cin >> T ;
    while(T)
    {
        X = 0, Y = 0 ;
        ++ d ;
        cin >> N ;
        cin >> fixed >> setprecision(5) ;
        for(int i = 1 ; i <= N ; ++ i)
            cin >> A[i];
        for(int j = 1 ; j <= N ; ++ j)
            cin >> B[j] ;


        sort(A + 1, A + N + 1) ;
        sort(B + 1, B + N + 1) ;

        for(int i = 1, j = 1; i <= N ; ++ i)
            if(A[i] > B[j])
            {
                ++ X ;
                ++ j ;
            }

        for(int i = 1, j = 1 ; i <= N ; ++ i)
            if(B[i] > A[j])
            {
                ++ Y ;
                ++ j ;
            }

        Y = N - Y ;
        cout << "Case #" << d << ": " << X <<' '<< Y << '\n';



        -- T ;
    }

    cin.close() ;
    cout.close() ;
    return 0 ;
}
