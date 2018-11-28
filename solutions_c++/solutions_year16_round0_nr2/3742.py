#include <bits/stdc++.h>

using namespace std;

int t ;
int n ;

int main()
{
    freopen("B-large.in","r",stdin) ;
    freopen("out.txt","w",stdout) ;
    scanf("%d",&t) ;
    string s ;
    for ( int c = 1 ; c <= t ; c++ )
    {
        cin >> s ;
        bool k = 0 ;
        int ans = 0 ;
        for ( int i = 0 ; i < s.size() ; i++ )
        {
            if ( s[i] == '+' && k )
                k = 0 , ans++;
            else if ( s[i] == '-' ) k = 1 ;
            if ( s[i] == '-' && i && s[i-1] == '+' ) ans++ ;
        }
        if ( k ) ans++ ;
        printf("Case #%d: %d\n",c,ans) ;
    }
    return 0;
}
