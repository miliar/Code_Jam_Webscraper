///Created by Gergely David.
///CNPR - Beclean
#include <fstream>


using namespace std ;


const int NMAX = 100 ;
const int INF = 0x3f3f3f3f ;

ifstream fin("input.in") ;
ofstream fout ("output.out") ;








int T ;
long long    A, K, B ;
int d  = 0;
long long  rez = 0 ;

int main()
{
    fin >> T ;

    while(T)
    {
        rez = 0 ;
        fin >> A >> B >>  K ;
        ++ d ;

        for(unsigned i = 0 ; i < A ; ++ i)
            for(unsigned j = 0 ; j < B ; ++ j)
                if((i & j) < K)
                    ++ rez ;
        fout << "Case #" << d << ": " ;
        fout << rez << '\n' ;

        -- T ;
    }


    fin.close() ;
    fout.close() ;
    return 0 ;
}




