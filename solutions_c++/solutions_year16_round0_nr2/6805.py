#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen( "B-large.in","r",stdin );
    freopen( "output.in","w",stdout );
    int t, T, ans;
    string s;
    cin >> t;
    for( T=1;T<=t;T++ ){
        cin >> s;
        int sz = s.size();
        int k = sz-1;
        ans=0;
        while( 1 ){
                if( s[k]=='-'){
                    ans++;
                    for( int i=0;i<=k;i++ ){
                        if( s[i]=='+')s[i] = '-';
                        else s[i] = '+';
                    }
                }else k--;
                if( k==-1 )break;
            }
            printf( "Case #%d: %d\n",T,ans );
        }
}
