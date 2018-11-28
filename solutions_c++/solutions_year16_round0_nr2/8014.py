#include <bits/stdc++.h>
#define N       105
using namespace std;

bool happy[N];

int main() {
    freopen( "B-large.in", "rt", stdin );
    freopen( "output.txt", "wt", stdout );
    int T, cases = 0;
    cin >> T;

    while ( T-- ){
        string s;
        cin >> s;

        for( int i = 0; i < s.size(); ++i )
            happy[i] = s[i] == '+';

        bool happy_before = false;
        bool sad_before = false;
        int flips = 0;
        for( int i = 0; i < s.size(); ++i ){
            if( happy[i] ){
                if ( sad_before ){
                    ++flips;
                    sad_before = false;
                }
                happy_before = true;
            }

            if( !happy[i] ){
                if ( happy_before ){
                    ++flips;
                    happy_before = false;
                }
                sad_before = true;
            }
        }

        if( sad_before )
            ++flips;

        cout << "Case #" << ++cases << ": " << flips << '\n';
    }
}
