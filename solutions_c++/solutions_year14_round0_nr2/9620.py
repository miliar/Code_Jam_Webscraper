#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std ;

ifstream fin("f.in") ;
ofstream fout("f.out") ;

int T ;
double C, F, X, sol ;
int d = 0 ;

int main()
{
fin >> T ;
while(T)
{
    double ido = 0 ;
    double init = 2.00000 ;
    double first, second, third ;
    ++ d ;
    fin >> fixed >> setprecision(5) ;
    fin >> C >> F >> X ;
    fout << "Case #"<< d<< ": " ;

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
    fout << fixed << setprecision(7) ;
    fout << ido << '\n' ;
    -- T ;
    }
fin.close() ;
fout.close() ;
return 0 ;
}
