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
 
#define N   112345

vector<pii> v;

int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int t;
    cin >> t;
    for(int qq = 1; qq <= t; qq++){
        int n;
        cin >> n;
        printf("Case #%d: ",qq);
        v.clear();
        for(int i = 0; i < n; i++){
            int x;
            cin >> x;
            v.push_back(mp(x,i));
        }
        sort(v.begin(),v.end());
        while(1){
            int maxx = 0;
            int cnt = 0;
            for(int i = n-1; i >= 0; i--){
                if( v[i].F > maxx ){
                    maxx = v[i].F;
                    cnt = 1;
                }
                else if( v[i].F == maxx ){
                    cnt++;
                }
            }
            if( maxx == 0 ){
                break;
            }
            if( cnt == 2 ){
                char ch1 = v[n-1].S + 'A';
                char ch2 = v[n-2].S + 'A';
                cout << ch1 << ch2 << " ";
                v[n-1].F--;
                v[n-2].F--;
            }
            else{
                char ch1 = v[n-1].S + 'A';
                v[n-1].F--;
                cout << ch1 << " ";
            }
            sort(v.begin(),v.end());
        }
        cout << endl;
    }
    return 0;
}