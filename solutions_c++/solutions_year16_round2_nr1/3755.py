// Author : Ankit Bisla
 
#include<bits/stdc++.h>
 
using namespace std;

#define     mp(x,y)     make_pair((x),(y))
#define     pb(x)       push_back(x)
#define     F           first
#define     S           second
#define     INF         (ll(1e9))
#define     INFL        (ll(1e18))
#define     EPS         1e-12
 
#define     chkbit(s, b)    (s & (1<<b))
#define     setbit(s, b)    (s |= (1<<b))
#define     clrbit(s, b)    (s &= ~(1<<b))

#define     p1d(a,n)          for(int ix=0;ix<n;ix++) printf("%d ",a[ix]); printf("\n");
#define     p2d(a,n,m)        for(int ix=1;ix<=n;ix++){ for(int jx=1;jx<=m;jx++) printf("%d ",a[ix][jx]); printf("\n");}
#define     ALL(A)          A.begin(), A.end()
 
#define     MOD         1000000007
 
#define gc getchar//_unlocked

#define     TRACE       1
 
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
 
typedef long long ll;
typedef unsigned long long ull;
 
#define vi vector<int>
#define pii pair<int,int>
 
#define N   30

string cur;

string s[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool possible(int x, int* a){
    int l = s[x].length();
    int req[30];
    for(int i = 0; i < 28; i++){
        req[i] = 0;
    }
    for(int i = 0; i < l; i++){
        req[s[x][i] - 'A']++;
    }
    for(int i = 0; i < l; i++){
        if( a[s[x][i] - 'A'] < req[s[x][i] - 'A'] ){
            return false;
        }
    }
    return true;
}

string ans;

bool go(int *a){
    bool f = false;
    int b[N];
    for(int i = 0 ;i < 10; i++){
        int l = s[i].length();
        if( possible(i,a) ){
            for(int j = 0; j < 26; j++){
                b[j] = a[j];
            }
            for(int j = 0; j < l; j++){
                a[s[i][j] - 'A']--;
            }

            f = true;
            if( go(a) ){
                ans += (char)(i + '0');
                return true;
            }
            else{
                for(int j = 0; j < 26; j++){
                    a[j] = b[j];
                }
            }
        }
    }
    bool g = false;
    for(int i = 0; i < 26;i++) {
        if( a[i] > 0 ){
            g = true;
        }
    }
    if( g ){
        return false;
    }
    return true;
}

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
        printf("Case #%d: ",qq);
        cin >> cur;
        int l = cur.length();
        int a[N];
        for(int i = 0; i < 28; i++) a[i] = 0;
        for(int i = 0; i < l; i++){
            a[cur[i]-'A']++;
        }
        ans = "";
        go(a);
        sort(ans.begin(),ans.end());
        cout << ans << endl;
    }
    return 0;
}