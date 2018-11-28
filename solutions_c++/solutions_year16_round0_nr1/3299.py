#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for ( int test = 1 ; test <= t ; ++ test )
    {
        int n;
        cin >> n;

        cout << "Case #" << test << ": ";
        int state = 0;

        if ( ! n )
            cout << "INSOMNIA";
        else
        {

            long long num = 0;

            while( state != 1023 )
            {
                num += n;
                string s = to_string(num);

                for ( char c : s )
                    state |= ( 1 << ( c - '0' ) );
            }
            cout << num;
        }
        cout << endl;
    }
    return 0;

}
