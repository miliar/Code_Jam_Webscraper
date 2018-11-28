#include <bits/stdc++.h>

using namespace std;

string S ,s ,a;
void f(int i)
{
    if ( i == s.size() )
    {
        S = max(S,a) ;
        return ;
    }
    a += s[i] ;
    f(i+1) ;
    a.pop_back() ;
    a = s[i] + a ;
    f(i+1) ;
    a = a.substr(1) ;
}
int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("OUT.txt","w",stdout) ;
    int t ;
    cin >> t ;
    string ans ;
    for ( int ct = 1 ; ct <= t ; ct++ )
    {
        S = "" ;
        cin >> s ;
        ans = "" ;
        ans += s[0] ;
        //f(0) ;
        for (int i = 1 ; i < s.size() ; i++ )
            if ( s[i] >= ans[0] ) ans = s[i] + ans ;
            else ans += s[i] ;
        cout << "Case #" << ct << ": " << ans << endl;
    }
    return 0;
}
