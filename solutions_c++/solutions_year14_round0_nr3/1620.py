#include <fstream>
#include <string.h>
#include <cstdlib>

using namespace std ;

const int NMAX = 65 ;

ifstream cin("minesweeper.in") ;
ofstream cout("minesweeper.out") ;

void Citire() ;
void Rezolvare() ;
void Afisare() ;
void Rezolvare_recursiva(int, int , int) ;
void Rezolvare_Problema() ;
bool Completeaza(int, int) ;


inline int max(int a, int b)
{
    if(a > b) return a ;
    else return b ;
}
inline int min(int a, int b)
{
    if(a < b) return a ;
    else return b ;
}

bool deschis[NMAX][NMAX] ;
bool mina[NMAX][NMAX] ;
bool minars[NMAX][NMAX] ;
bool deschisjocu[NMAX][NMAX] ;
bool deschismina[NMAX][NMAX] ;

int T, N, M, bombe;
int d = 0 ;
int X, Y, XX, YY ;
bool imposibil_posibil ;
bool rezolvare ;
int dupadeschidere ;

inline void Citire()
{
    cin >> T ;
    while(T)
    {

        cin >> N >> M >> bombe ;
        imposibil_posibil = true ;
       // memset(deschis, false, sizeof(deschis)) ;
        //memset(mina, false, sizeof(mina)) ;

        for(int i = 0 ; i < NMAX ; ++ i)
            for(int j = 0 ; j < NMAX ; ++ j)
        {
            deschis[i][j] = false ;
            mina[i][j] = false ;
        }
       Rezolvare_recursiva(bombe, 0, 0) ;

       // Rezolvare() ;


         ++ d ;
    cout << "Case #" << d << ": " << "\n" ;
    if(imposibil_posibil == true)
        cout << "Impossible" << "\n" ;
    else
    {
        for(int i = 0 ; i < N ; ++ i) {
            for(int j = 0 ; j < M ; ++ j)
               {

               if(minars[i][j] == true)
                    cout << "*";
                else
                {
                    if(i == X && j == Y)
                        cout << "c" ;
                    else
                        cout << "." ;
                }
        }
        cout << "\n" ;  }
    }

       // Afisare() ;
        -- T ;
    }
}

inline bool Completeaza(int Xi, int Yi)
{
    if( Xi > 0)
    {
        if (Yi > 0)
            if(mina[Xi - 1][Yi - 1] == true)
                return true ;
        if(Yi < M - 1)
            if(mina[Xi - 1][Yi + 1] == true)
                return true ;
        if(mina[Xi - 1][Yi] == true)
            return true ;
    }


    if(Xi < N - 1)
    {
        if(Yi > 0)
            if(mina[Xi + 1][Yi - 1] == true)
                return true ;
        if(Yi < M - 1)
            if(mina[Xi + 1][Yi + 1] == true)
                return true ;
        if(mina[Xi + 1][Yi])
            return true ;
    }


    if(Yi > 0)
    {
        if(mina[Xi][Yi - 1] == true)
            return true ;
    }



    if(Yi < M - 1)
    {
        if(mina[Xi][Yi + 1] == true)
            return true ;
    }

    return false ;

}

inline void Rezolvare_Problema()
{
    rezolvare = false ;

    for(int i = 0 ; i < N ; ++ i)
        for(int j = 0 ; j < M ; ++ j)
        {
            deschisjocu[i][j] = deschis[i][j] ;
            deschismina[i][j] = mina[i][j] ;
        }

    for(int ii = 0 ; ii < N ; ++ ii)
        for(int jj = 0 ; jj < M ; ++ jj)
            if(mina[ii][jj] == false && imposibil_posibil == true)
            {
                rezolvare = true ;
                deschis[ii][jj] = true ;
                dupadeschidere = 1;
                while(dupadeschidere != 0)
                {
                    dupadeschidere = 0;

                    for(int i = 0 ; i < N ; ++ i)
                        for(int j = 0 ; j < M ; ++ j)
                       if(mina[i][j] == false && deschis[i][j] == true)
                        {
                            XX = i ;
                            YY = j ;
                            if(Completeaza(i, j) == false)
                            {
                                if( YY > 0)
                                    if(deschis[XX - 1][YY - 1] == false)
                                    {
                                        ++ dupadeschidere ;
                                        deschis[XX - 1][YY - 1] = true ;
                                    }
                                if(YY < M - 1)
                                    if(deschis[XX - 1][YY + 1] == false)
                                    {
                                        ++ dupadeschidere ;
                                        deschis[XX - 1][YY + 1] = true ;
                                    }
                                if(deschis[XX - 1][YY] == false)
                                {
                                    ++ dupadeschidere ;
                                    deschis[XX - 1][YY] = true ;
                                }


                                if(XX < N - 1)
                                {
                                    if(YY > 0)
                                        if(deschis[XX + 1][YY - 1] == false)
                                        {
                                            ++ dupadeschidere ;
                                            deschis[XX + 1][YY - 1] = true ;
                                        }
                                    if(YY < M - 1)
                                        if(deschis[XX + 1][YY + 1] == false)
                                        {
                                            ++ dupadeschidere ;
                                            deschis[XX + 1][YY + 1] = true ;
                                        }
                                    if(deschis[XX + 1][YY] == false)
                                    {
                                        ++ dupadeschidere ;
                                        deschis[XX + 1][YY] = true ;
                                    }


                                }

                                if(YY > 0)
                                {
                                    if(deschis[XX][YY - 1] == false)
                                    {
                                        ++ dupadeschidere ;
                                        deschis[XX][YY - 1] = true ;
                                    }
                                }

                                if(YY < M - 1)
                                {
                                    if(deschis[XX][YY + 1] == false)
                                    {
                                        ++ dupadeschidere ;
                                        deschis[XX][YY + 1] = true ;
                                    }
                                }


                            }
                        }

                    for(int i = 0 ; i < N ; ++ i)
                        for(int j = 0 ; j < M ; ++ j)
                            if(deschis[i][j] == false )
                            {
                                rezolvare = false;
                                break ;
                            }
                    if(rezolvare == true)
                    {
                        for(int i = 0 ; i < N ; ++ i)
                            for(int j = 0 ; j < M ; ++ j)
                                minars[i][j] = deschismina[i][j] ;
                        X = ii ;
                        Y = jj ;
                        imposibil_posibil = false ;
                        break ;
                    }
                    for(int i = 0 ; i < N ; ++ i)
                        for(int j = 0 ; j < M ; ++ j)
                        {
                            deschis[i][j] = deschisjocu[i][j] ;
                            mina[i][j] = deschismina[i][j] ;
                        }

                }
            }
}



void Rezolvare_recursiva(int nr, int l, int c)
{


    if(imposibil_posibil == true)
    {
        for(int i = 1 ; i >= 0 ; i --)
           {

           if(i == 0)
            {
                if(nr == 0)
                    Rezolvare_Problema() ;
                else
                {
                    if(l == N - 1 && c == M - 1 )
                       {

                       }
                    else
                    {
                        if(c == M - 1)
                            Rezolvare_recursiva(nr, l + 1, 0) ;
                        else Rezolvare_recursiva(nr, l, c + 1) ;
                    }
                }
            }
            else if(i == 1 && mina[l][c] == false)
            {
                mina[l][c] = true ;
                deschis[l][c] = true ;
                -- nr ;
                if(nr == 0)
                    Rezolvare_Problema() ;
                else
                {
                    if(l == N - 1 && c == M - 1 )
                        {

                        }
                    else
                    {
                        if(c == M - 1)
                            Rezolvare_recursiva(nr, l + 1, 0) ;
                        else Rezolvare_recursiva(nr, l, c + 1) ;
                    }
                }
                mina[l][c] = false ;
                deschis[l][c] = false ;
                ++ nr ;

            }


    }
    }


}


int main()
{
    Citire() ;
    cin.close() ;
    cout.close() ;
    return 0 ;
}
