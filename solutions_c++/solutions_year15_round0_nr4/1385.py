#include <bits/stdc++.h>

using namespace std ;


ifstream in("input.in") ;
ofstream out("output.out") ;

int X, R, C, RC;
int T ;


int main()
{
    in >> T ;

    for(int cs = 1 ; cs <= T ; ++ cs)
    {
        out << "Case #" << cs << ": ";
        in >> X >> R >> C ;
        RC = R * C ;

        if(X == 1)
            out << "GABRIEL\n" ;
        if(X == 2)
        {

            if(RC % 2 == 0)
                out << "GABRIEL\n" ;
            else out << "RICHARD\n" ;
        }
        if(X == 3)
        {
            if(RC == 6 || RC == 9 || RC == 12)
                out << "GABRIEL\n" ;
            else out << "RICHARD\n" ;
        }

        if(X == 4)
        {
            if(RC == 12 || RC == 16)
                out << "GABRIEL\n" ;
            else out << "RICHARD\n" ;

        }

    }

    in.close() ;
    out.close() ;
    return 0 ;
}
