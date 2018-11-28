#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t , n ;
    string s ;
    scanf("%d",&t);
    int SUM , ans ;
    for ( int x = 1 ; x<= t; x++ ) {
        cin >> n >> s ;
        SUM = ans = 0 ;
        for ( int j = 0 ; j < s.size() ; j++ ) {
            if ( s[j]-'0' ) {
                if ( j > SUM + ans )
                    ans += j-SUM-ans ;
                SUM += s[j]-'0' ;
            }
        }
        printf("Case #%d: %d\n",x,ans);
    }
    return 0;
}

