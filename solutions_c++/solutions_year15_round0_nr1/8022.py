#include<bits/stdc++.h>

using namespace std;

int main()
{

    freopen( "A-large.in" , "r" , stdin );
    freopen( "LargeOutputattempt0.txt" , "w" , stdout );

    int t;
//    cin>>t;
    scanf ("%d", &t);

    int sm;
    char s[1005];

    int j;
    int np;
    int i;
    int req;

    for ( j = 1 ; j <= t ; j++ )
    {
//        cin>>sm;
//        cin>>s;

        scanf ("%d", &sm);
        scanf ("%s", s);

        np = 0;
        req = 0;

        for ( i = 0 ; i <= sm ; i++ )
        {
            if ( np >= i )
            {
                np += s[i] - '0';

                if ( s[i] == '0' && np == i )
                {
                    req++;
                    np++;
                }
            }
        }

//        cout<<"Case #"<<j<<": ";
//        cout<<req<<endl;

        printf ("Case #%d: %d\n", j, req);
    }

    return 0;
}
