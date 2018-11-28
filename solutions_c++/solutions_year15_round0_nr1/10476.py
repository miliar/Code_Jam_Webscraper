#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std ;

int main(void)
{
    freopen("A-small-attempt2.in" , "r" , stdin) ;
    freopen("out.txt" , "w" , stdout) ;

    int T ; cin >> T ;
    for(int t = 1 ; t <= T ; t++)
    {
        int smax ; cin >> smax ;


            int nowstand = 0 , call = 0 ;
            char aud[1200] ; cin >> aud ;
            cout << "Case #" << t << ": " ;
            for(int i = 0 ; i <= smax ; i++)
                if(aud[i] != '0')
                {
                    if(i > nowstand)
                    {
                        call = i - nowstand ;
                        nowstand += call ;
                    }
                    nowstand += aud[i] - '0' ;
                }
            cout << call ;

        cout << "\n" ;
    }
	return 0;
}
