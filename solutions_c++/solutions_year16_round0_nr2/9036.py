#include<bits/stdc++.h>
using namespace std;

#define DEBUGN

int main() {

    freopen("input.in", "r", stdin);
#ifndef DEBUG
    freopen("output.txt", "w", stdout);
#endif // DEBUG

    int t;  cin>>t;
    for( int tt=1; tt<=t; ++tt ) {
        string s;   cin>>s;

        int ans = 0;
        while ( true ) {
            int i=0;

            int downupflag = false;
            while( i != s.length() && s[i] == '-' ) {
                s[i++] = '+';
                if( not downupflag )
                    downupflag = true;
            }
            if( downupflag ) {
                ans++;
                continue;
            }


            while( i != s.length() && s[i] == '+' ) {
                s[i++] = '-';
            }
            if( i == s.length() ) {
                break;
            } else {
                ans++;
            }

        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
