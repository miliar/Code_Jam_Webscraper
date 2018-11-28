
#include<iostream>
#include<string.h>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


    string s;
    int j, i, ans, t, k, len, tmp;
    cin >>t;
    for( j = 1; j <= t; j++ ) {
        cin>>s;
        ans = 0;
        if( s.length() == 1 ) {
            if( s[0] == '-')
                ans = 1;
        }
        else {
            for( i = s.length() - 1; s[i] != '-' && i >= 0; i-- ) {}
            len = i;
            while( len > -1 ) {
                if( s[0] == '-') {
                    for( k = 0, i = len; k <= len/2; k++, i-- ) {
                        tmp = s[i];
                        s[i] = s[k];
                        s[k] = tmp;
                    }
                    for( k = 0; k <= len; k++ ) {
                        if( s[k] == '-')
                            s[k] = '+';
                        else
                            s[k] = '-';
                    }
                    for( i = len-1; s[i] != '-' && i >= 0; i-- ) {}
                    len = i;
                }
                else {
                    for( i = 0; s[i] != '-'; i++)
                        s[i] = '-';
                }

                ans++;
            }
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
