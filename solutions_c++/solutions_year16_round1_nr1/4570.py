#include <bits/stdc++.h>
using namespace std ;

int cse ;
deque < char > ans ;
string s ;
int main()
{
    freopen("A.txt", "r", stdin);
    freopen("AA.txt", "w+", stdout);

    int t ;
    scanf("%d", &t) ;
    while(t--)
    {
        ans.clear() ;
        //cout << t << endl ;

        cin >> s ;
        int sz = s.size() ;
        ans.push_back(s[0] ) ;
        for( int i = 1 ; i < sz ; i++ )
        {
            if( ans.front() <= s[i] ) ans.push_front(s[i] ) ;
            else ans.push_back( s[i] ) ;
        }
        cout << "Case #"<< ++cse << ": " ;
        for( int i = 0 ; i < sz ; i++ )
        {
            printf("%c", ans[i] ) ;
        }
        cout << endl ;

    }

}
