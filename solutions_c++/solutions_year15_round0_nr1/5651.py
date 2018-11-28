#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
main()
    {int T, t, S, s[1000], i, p=0, f=0;
    char c;

    cin >> T;

    for (t=1; t<= T; t++)
        {cin >> S;
        p=0;
        f=0;

        for(i=0; i<=S; i++)
            {scanf(" %c", &c);
            s[i] = c-48;}

        p = s[0];
        for(i=1; i<=S; i++)
            {if (p+f<i)
                f += i - p - f;
            p += s[i];}


        cout << "Case #" << t << ": " << f << endl;}

    return 0;}
