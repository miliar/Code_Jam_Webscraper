#include <iostream>
#include <cstring>

using namespace std;

main()
{
    int T ;
    cin >> T ;
    cin.get() ;
    for(int a = 0 ; a < T ; a++)
        {
        int ile = 0 , s ;
        char S[102] = {} ;
        cin.getline(S,101) ;
        s = strlen(S) ;
        for(int a = 1 ; a < s ; a++)
            {
            if(S[a] != S[a-1]) ile ++ ;
            }
        if(S[s-1] == '-' && s > 1) ile ++ ;
        else if(s == 1 && S[0] == '-') ile = 1 ;
        cout << "Case #" << a + 1 << ": " << ile << endl ;
        }
    return 0 ;
}
