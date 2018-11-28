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

ll pw (ll n, ll s)
{
    if (s==0) return 1;
    if (s==1) return n;
    if (s%2==1) return n*pw(n,s-1);
    ll o = pw(n,s/2);
    return o * o;
}

string tod(int n, int s)
{
    string res;
    while(n)
    {
        res+=char(n%2+48);
        n/=2;
    }
    rev(all(res));
    while(s>res.size()) res="0"+res;
    return res;
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
        ll n,j;
        ll primeNum[]={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
        cin>>n>>j;
        cout<<"Case #"<<Q+1<<":\n";
        forn(num,(1<<n-2))
        {
            string r = tod(num,n-2);
            r="1"+r+"1";
            vector <ll> div;
            forr(base,2,10)
            {
                forn(i,20)
                {
                    ll k=0;
                    forn(pos,n)
                    {
                        k+=(pw(base,pos)*(r[n-1-pos]-'0'))%primeNum[i];
                    }
                    k%=primeNum[i];
                    if (k==0) {div.pb(primeNum[i]);break;}
                }
            }
            if (div.size()==9)
            {
                j--;
                cout<<1;
                cout<<tod(num,n-2);
                cout<<1<<' ';
                forn(i,9) cout<<div[i]<<' ';
                cout<<endl;
                div.clear();
            }
            if (j==0) break;
        }
        cout<<endl;
    }
    return 0;
}
