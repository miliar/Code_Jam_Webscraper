#pragma comment(linker,"/STACK:100000000000,100000000000")

#define _CRT_SECURE_NO_WARNINGS

#include <bits/stdc++.h>

#define ll long long
#define pb push_back
#define mp make_pair
#define D long double
#define pi pair<int,int>
#define F first
#define S second
#define forn(i,n) for (int(i)=0;(i)<(n);i++)
#define forr(i,x,y) for (int(i)=(x);(i)<=(y);i++)
#define ford(i,x,y) for (int(i)=(x);(i)>=(y);i--)
#define rev reverse
#define in insert
#define er erase
#define all(n) (n).begin(),(n).end()
#define graf vector<vector<pi> >
#define graf1 vector<vector<ll> >
#define sqr(a) (a)*(a)
#define file freopen("password.in","r",stdin);freopen("password.out","w",stdout);
#define y1 asdadasdasd

const int INF = 1e9;
const D cp = 2 * asin(1.0);
const D eps = 1e-9;
const ll mod = 1000000007;

using namespace std;

void div(ll n, set<int> &dig)
{
    if (n==0) {dig.in(0);return;}
    while(n)
    {
        dig.in(n%10);
        n/=10;
    }
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    /*freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);*/
    int T;
    cin>>T;
    forn(Q,T)
    {
        ll n;
        cin>>n;
        set<int> dig;
        ll res=-1;
        forr(i,1,10000)
        {
            div(i*n,dig);
            if (dig.size()==10) {res=i;break;}
        }
        cout<<"Case #"<<Q+1<<": ";
        if (res==-1) cout<<"INSOMNIA"; else cout<<res*n;
        cout<<endl;
    }
    return 0;
}
