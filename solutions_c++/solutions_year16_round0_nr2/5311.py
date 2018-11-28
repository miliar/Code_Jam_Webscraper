///*********************************************************************

#include <cstring>
#include <fstream>
#include <cstdio>
#include <iostream>

using namespace std ;



///*********************************************************************

string s ;


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

        cin >> s ;

        int cnt = 0 ;
        for(int i = 0 ; i < s.size() - 1 ; ++ i )
            if(s[i] != s[i + 1])
                cnt ++ ;

        if(s[s.size() - 1] == '-')
            cnt ++ ;
        cout << "Case #" << testCase << ": " <<  cnt << '\n' ;



    }

    return 0 ;
}
