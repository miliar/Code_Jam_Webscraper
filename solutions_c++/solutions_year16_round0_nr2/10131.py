#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define bg begin()
#define en end()
#define debug cout << "YES" << endl

using namespace std;

typedef pair<int,int>II;
template<class T> int getbit(T s, int i)
{
    return (s >> i) & 1;
}
template<class T> T onbit(T s, int i)
{
    return s | (T(1) << i);
}
template<class T> T offbit(T s, int i)
{
    return s & (~(T(1) << i));
}
template<class T> int cntbit(T s)
{
    return __builtin_popcount(s);
}
template<class T> T gcd(T a, T b)
{
    T r;
    while (b != 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

const long double PI = 2*acos(0.0);
const long double eps = 1e-15;
const int infi = 1e9;
const ll Linfi = 1e18;
const ll mod = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 200005

ll t;
ll a[11];
string s;
void solve()
{
    cin>>t;
    ll c = 1;
    while(t--)
    {
        cin>>s;
        ll flip = 1;
        ll dem = 0;
        FORD(i,s.size()-1,0){
            ll t;
            if(s[i]=='-') t=-1*flip;
            else t = flip;
            if(t==-1){ dem++; flip*=-1; }
        }
        cout<<"Case #"<<c<<": "<<dem<<endl;
        c++;
    }

}

int main()
{
    ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    //freopen("B-small-attempt2.in","r",stdin);
    //freopen("B-small-attempt2.out","w",stdout);
#endif

    solve();

    return 0;
}

