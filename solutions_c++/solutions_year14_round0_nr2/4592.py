#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std ;

ifstream cin("cookie.in") ;
ofstream cout("cookie.out") ;

int T ;
double C, F, X, sol ;
int d = 0 ;

int main()
{
    cin >> T ;
    while(T)
    {
        double ido = 0 ;
        double init = 2.00000 ;
        double first, second, third ;
        ++ d ;
        cin >> fixed >> setprecision(5) ;
        cin >> C >> F >> X ;
        cout << "Case #"<< d<< ": "  ;

        bool ok = true ;

        while(ok)
        {
            first = X / init ;
            second = C / init ;
            third = X / (init + F) ;
            if(second + third > first)
            {
                ok = false ;
            }
           else
           {
               ido = ido + C / init ;
               init = init + F ;
           }

        }
       ido = ido + ( X / init) ;
        cout << fixed << setprecision(7) ;
        cout << ido << '\n' ;
        -- T ;
    }
    cin.close() ;
    cout.close() ;
    return 0 ;
}
