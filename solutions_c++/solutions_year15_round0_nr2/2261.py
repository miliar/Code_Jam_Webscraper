

#include <bits/stdc++.h>

using namespace std ;

const int NMAX = 10005  ;
const int INf = 0x3f3f3f3f ;

ifstream in("input.in") ;
ofstream out("output.out") ;

int T ;
int D, P[NMAX];
int N,   MAX = -INf , ADD, AUX ;

int main()
{

    in >> T ;

    for(int cs = 1 ; cs <= T ; ++ cs)
    {
        out << "Case #" << cs << ": " ;

        in >> D ;
        MAX = -INf;

        for(int i = 1 ; i <=D; ++ i )
        {
            in >> P[i] ;
            if(MAX < P[i])
                MAX = P[i] ;
        }



        AUX = MAX ;



        for(int i = 1 ; i <= MAX; ++ i )
        {
            ADD = i ;

            for(int j = 1 ; j <=D; ++ j )
            {
               if(P[j] > i )
                    if(P[j] % i  == 0)
                        ADD = ADD + (P[j] / i - 1) ;
                    else ADD = ADD + (P[j] / (i)) ;


            }

            AUX = min(AUX, ADD) ;
        }


        out << AUX << '\n' ;
    }


    in.close() ;
    out.close() ;
    return  0 ;
}
