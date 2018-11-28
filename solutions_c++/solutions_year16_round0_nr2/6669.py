#include <bits/stdc++.h>

using namespace std;

int main(){

    int T;
    string s;

    freopen( "inputLB.in", "r", stdin );
	freopen( "outputLB.txt", "w", stdout );

    cin >> T;

    for( int t= 1; t<= T; ++t ){

        cin >> s;
        int ans= 0;
        int n= (int)s.length();

        for( int i= n-1; i>= 0; --i ){

            if( s[i]== '-' ){

                for( int j= i; j>= 0; --j ){
                    if( s[j]== '-' )
                        s[j]= '+';
                    else
                        s[j]= '-';
                }

                ans++;
            }

        }

        cout << "Case #" << t << ": " << ans << '\n';

    }


}
