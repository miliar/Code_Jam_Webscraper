#include <bits/stdc++.h>


using namespace std ;

ifstream in("input.in") ;
ofstream out("output.out") ;

string sir ;
int T, N, var, act, cnt;

int main()
{

    in >> T ;

    for(int i = 1 ; i <= T ; ++ i)
    {
        out << "Case #" << i << ": " ;

        in >> N >> sir ;
        cnt = sir[0] - '0' ;
        var = 0 ;
        for(int ii = 1 ; ii <= N ; ++ ii) {
            act = sir[ii] - '0' ;
            if(act == 0 )
                continue ;
            if(cnt < ii )
            {

                var += (ii - cnt) ;
                cnt += (ii - cnt) ;



            }

            cnt += act ;
        }

        out << var << '\n' ;
    }

    return  0 ;
}
