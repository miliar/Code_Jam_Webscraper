///*********************************************************************

#include <cstring>
#include <fstream>
#include <cstdio>
#include <iostream>

using namespace std ;



///*********************************************************************

  long long K, C, S;


///*********************************************************************

///Ridicare la putere in timp logaritmic

  long long  power(long long N, long long K)
{

    if(K == 0)
        return 1 ;
    if(K % 2 == 0)
        return power(N * N, K / 2) ;
    else return N * power(N * N, (K - 1) / 2) ;
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
    cin >> T ;
    for(int testCase = 1 ; testCase <= T ; ++ testCase)
    {
        cout << "Case #" << testCase << ": " ;

        cin >> K >> C >> S ;



        long long ant = 0;
        long long cnt = 0 ;



    for(int i = 1 ; i <= S ; i++)
    {
        cout << i << ' '  ;
    }
    cout << '\n' ; }



    return 0 ;
}
