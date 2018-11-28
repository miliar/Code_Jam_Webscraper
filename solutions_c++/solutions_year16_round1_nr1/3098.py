#include <bits/stdc++.h>
using namespace std;
#define ll long long

#define N 2123456

#define     TRACE           1

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
        string s;
        cin >> s;
        int l = s.length();
        string ans = "";
        ans += s[0];
        for(int i = 1; i < l; i++){
            if( s[i] >= ans[0] ){
                ans = s[i] + ans;  
            }
            else{
                ans = ans + s[i];
            }
        }
        cout << "Case #" << qq << ": " << ans << "\n";
    }
    return 0;
}