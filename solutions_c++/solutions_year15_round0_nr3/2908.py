#include <iostream>
#include <map>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

char f(char a , char b ) {
    if ( a == 'a' ) {
        if ( b == 'a' )
            return 'a' ;
        else if ( b == 'i' )
            return 'i' ;
        else if ( b == 'j' )
            return 'j' ;
        else
            return 'k' ;
    }
    else if ( a == 'z' ) {
        if ( b == 'a' )
            return 'z' ;
        else if ( b == 'i'  )
            return 'I' ;
        else if ( b == 'j' )
            return 'J' ;
        else
            return 'K' ;
    }
    else if ( a == 'i' ) {
        if ( b == 'a'  )
            return 'i' ;
        else if ( b == 'i' )
            return 'z' ;
        else if ( b == 'j' )
            return 'k' ;
        else
            return 'J';
    }
    else if ( a == 'I' ){
        if ( b == 'a' )
            return 'I' ;
        else if ( b == 'i' )
            return 'a' ;
        else if ( b == 'j' )
            return 'K' ;
        else
            return 'j' ;
    }
    else if ( a == 'j' ) {
        if ( b == 'a' )
            return 'j' ;
        else if ( b == 'i' )
           return 'K' ;
        else if ( b == 'j' )
            return 'z' ;
        else
            return 'i' ;
    }
    else if ( a == 'J' ) {
        if ( b == 'a' )
            return 'J' ;
        else if ( b == 'i' )
            return 'k' ;
        else if ( b == 'j' )
            return 'a' ;
        else
            return 'I' ;
    }
    else if ( a == 'k' ) {
        if ( b == 'a' )
            return 'k' ;
        else if ( b == 'i' )
            return 'j' ;
        else if ( b == 'j' )
            return 'I';
        else
            return 'z' ;
    }
    else {
        if ( b == 'a' )
            return 'K' ;
        else if ( b == 'i' )
            return 'J' ;
        else if ( b == 'j' )
            return 'i' ;
        else
            return 'a' ;
    }
}
int main()
{
    int t ;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    string s , tmp , ans  ;
    int n , x ;
    cin >> t ;
    for ( int z = 1 ; z <= t ; z++ ) {
        cin >> n >> x >> tmp ;
        s = "" ;
        ans = "" ;
        bool sol = 0  ;
        for ( int i = 0 ;i < x ; i++ )
            s += tmp ;
        tmp = "" ;
        int mi = 0 ;
        tmp += s[0] ;
        ans += s[0] ;
        char c;
        for ( int i = 1 ; i < s.size() ; i++ ) {
            c = f(tmp[0],s[i] );
            ans += c ;
            tmp[0] = c;
        }
        if ( ans[ans.size()-1] != 'z' ) {
            printf("Case #%d: NO\n",z);
        }
        else {
            for ( int i = 0 ; i < ans.size() ; i++ ) {
                if ( ans[i] == 'i' ) {
                    for ( int j = i+1 ; j < ans.size() ; j++ ) {
                        if ( ans[j] == 'k' )
                            sol = 1 ;
                    }
                    break;
                }
            }
            if ( sol ) {
                printf("Case #%d: YES\n",z);
            }
            else {
                printf("Case #%d: NO\n",z);
            }
        }
    }
    return 0;
}
