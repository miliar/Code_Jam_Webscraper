#include <iostream>
//#include <cstdio>
#include <string>

using namespace std;

main()
{


    int T, t, C, n, flips;
    string S;

    cin >> T;

    for(t=1; t<=T; t++)
    {
        cin >> S;
        flips = 0;

        for(int i=0; i<(S.size()-1); i++)
            {if (S[i] != S[i+1])
            flips++;}
        if(S[S.size()-1] == '-')
            flips++;




        cout<< "Case #" << t << ": " << flips << endl;
    }
    return 0;
}
