#include <bits/stdc++.h>

using namespace std;

int min_flips(string&);

int main()
{
    int t;
    cin >> t;

    for ( int test = 1 ; test <= t ; ++ test )
    {
        string s;
        cin >> s;

        cout << "Case #" << test << ": " << min_flips(s) << endl;
    }
    return 0;
}

int min_flips(string &s)
{
    const int n = s.length();

    int b = ( s.front() == '+' );
    int h = ! b;

    for ( int i = 1 ; i < n ; ++ i )
    {
        if ( s[i] == '+' )
        {
            if ( s[i - 1] == '-' )
                b += 2;
        }
        else
        {
            if ( s[i - 1] == '+' )
                h += 2;
        }
    }
    return min( b + 1, h );
}
