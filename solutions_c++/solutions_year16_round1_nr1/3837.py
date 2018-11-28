#include<bits/stdc++.h>
using namespace std;

typedef long long int lld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <ll> vl;
typedef pair <ll, ll> pll;
const double PI = acos(-1);

//defines
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define mem(a, b) memset(a, b, sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a)*(a))
#define inf 100000000
#define mod 1000000007
#define EPS 1e-9
#define nl puts("")
#define odd(n) (n&1)
#define even(n) (!(n&1))

//loop
#define rep(i, n) for(int i = 0; i < n; ++i)
#define REP(i, n) for(int i = 1; i <= n; ++i)

//input
#define si(a) scanf("%d", &a)
#define sii(a, b) scanf("%d%d", &a, &b)
#define siii(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sl(a) scanf("%lld", &a)
#define sll(a, b) scanf("%lld%lld", &a, &b)
#define slll(a, b, c) scanf("%lld%lld%lld", &a, &b, &c)
#define sd(a) scanf("%lf", &a)
#define sc(a) scanf("%c", &a)
#define sst(a) scanf("%s", a)

#define MX 1000010



template <class T>
        inline void debug (const T& x,const T& y=0,const T& z=0)
        {
            cout<<">> "<<x<<" "<<y<<" "<<z<<endl;
        }

main()
{
    freopen("inL.txt","r",stdin);
    freopen("outL.txt","w",stdout);

    list <char> L;
    lld i,j,n,T,cs;
    string s;
    cin>>T;

    REP(cs,T)
    {
        cin>>s;

        L.push_back(s[0]);

        for(i=1;i<s.size();i++)
        {
            //cout<<">"<<L.front()<<endl;
            if(L.front()<=s[i])
                L.push_front(s[i]);
            else if(L.front()>s[i])
                L.push_back(s[i]);
        }

        list<char>::iterator it;

        cout<<"Case #"<<cs<<": ";

        for(it=L.begin();it!=L.end();it++)
            cout<<*it;
        cout<<endl;

        L.clear();
    }
    return 0;
}


