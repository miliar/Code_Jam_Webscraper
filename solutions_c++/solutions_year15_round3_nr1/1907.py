#include <bits/stdc++.h>
using namespace std;

#define TRACE

#ifdef TRACE
    #define trace1(x)                cerr << #x << ": " << x << endl;
    #define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
    #define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
    #define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
    #define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
    #define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

    #define trace1(x)
    #define trace2(x, y)
    #define trace3(x, y, z)
    #define trace4(a, b, c, d)
    #define trace5(a, b, c, d, e)
    #define trace6(a, b, c, d, e, f)

#endif

#define ll long long
#define Sl(x) scanf("%lld",&x)
#define Su(x) scanf("%llu",&x)
#define all(v) v.begin(),v.end()
#define Sc(x) scanf("%d",&x)
#define P(x) printf("%d", x)
#define nl() printf("\n");
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mii map<int,int>
#define pps pair<ll,pll>
#define ppi pair<pii,int>
#define ppf pair<pll,ll>
#define psi pair<string,int>
#define pis pair<int,string>
#define F first
#define S second
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define mem(x,i) memset(x,i,sizeof(x))
#define fori(i,s,n) for(int i=(s);i<(n);++i)
#define ford(i,s,n) for(int i=(n)-1;i>=(s);--i)
#define INF 8944674407370955161LL
#define debug(i,st,arr) fori(i,0,st){cout<<arr[i]<<" ";}cout<<endl;
#define forci(i,sw) for((i)=(sw).begin();(i)!=(sw).end();(i)++)
#define forcd(i,sw) for((i)=(sw).rbegin();(i)!=(sw).rend();(i)++)

ll abs(ll x) {if(x < 0) return -x; return x;}

int addmod(int v1, int v2) {
    int v3 = v1+v2;
    if(v3 >= MOD) v3 -= MOD;
    return v3;
}

int rec(int c, int w)
{
    if(w == 1)
        return c;
    if(w == c)
     {
        return w;
     }
     else if(w == c/2)
     {
         if(c%2)
            return 2+w;
         else
            return 1+w;
     }
     else if(w > c/2)
     {
        return w+1;
     }
	if(c-2*w < w)
	{
		return 1+w+1;
	}
	if(c-2*w == w)
		return 2 + w;
	return 2+rec(c-2*w, w);
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int t, r, c, w;
	cin>>t;
	for(int tc = 1; tc <= t; ++tc)
	{
		 cout<<"Case #"<<tc<<": ";
		 cin>>r>>c>>w;
		 /*if(w == c)
		 {
		 	cout<<w<<endl;
		 }
		 else if(w == c/2)
         {
            cout<<1+w<<endl;
         }
		 else if(w >= c/2)
         {
            cout<<w<<endl;
         }
		 else
		 {
		 	int ans = r-1;
		 	ans += rec(c, w);
		 	// if(c-2*w < w)
		 	// {
		 	// 	ans += 1+w;
		 	// }
		 	// else if(c-2*w == w)
		 	// {
		 	// 	ans += 2+w;
		 	// }
		 	// else
		 	// {
		 	// 	ans +=
		 	// }
		 	cout<<ans<<endl;
		 }*/
		 int ans = r-1;
		 ans += rec(c, w);
		 cout<<ans<<endl;
	}
    return 0;
}
