///*********************************************************************

#include <cstring>
#include <fstream>
#include <cstdio>
#include <iostream>

using namespace std ;

///*********************************************************************

const int NMAX = 10 ;
int C[NMAX];

///*********************************************************************

///Cifrele unui numar

void cifra(long long nr, int &size_H)
{

    while(nr > 0 )
    {
        int last_digit = nr % 10 ;

        if(C[last_digit] == 0)
        {
            size_H ++ ;
            C[last_digit] = 1 ;
        }
        nr = nr / 10 ;
    }

}

///*********************************************************************

///Functia principala!

int main()
{

#ifndef ONLINE_JUDGE

    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

#endif // ONLINE_JUDGE

    int T;
    long long nr ;
    cin >> T ;
    for(int testCase = 1 ; testCase <= T ; ++ testCase)
    {

        cout << "Case #" << testCase << ": " ;

        memset(C, 0, sizeof C) ;
        int size_H = 0 ;
        cin >> nr ;
        int cod = 1 ;
        long long trr = 0 ;
        do
        {
            if(nr == 0)
                break ;
            cifra(cod * nr, size_H) ;
            trr = cod * nr ;
            cod ++ ;
        }
        while(size_H != 10);

        if(size_H == 10)
            cout << trr << "\n" ;
        else cout << "INSOMNIA\n" ;

    }

    return 0 ;
}
