/*******************************\
   Name:    REAJUL HAQUE REAYZ  |
   School:  COMILLA UNIVERSITY  |
            CSE (5TH BATCH)     |
********************************/
#include<bits/stdc++.h>
#define ll long long int
#define mem(x,y) memset(x,y,sizeof(x))
#define sfi(n) scanf("%d",&n)
#define sfs(n) scanf("%s",n)
#define pfi(n) printf("%d",n)
#define pfs(n) printf("%s",n)
#define pfne() printf("\n")
#define pfsp() printf(" ")
#define lld I64d
#define endl "\n"
#define inf 1<<30;
#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define ss stringstream
#define pi 2*acos(0.0)
#define Pi acos(-1)
#define PI 3.1415926535897932384626433832795
#define bit_cnt(mask) __builtin_popcount(mask)
using namespace std;
template < class T > inline T gcd(T a,T b) {a=abs(a);b=abs(b); if(!b) return a; return __gcd(b,a%b);}
template < class T > inline T lcm(T a,T b) {a=abs(a);b=abs(b); return (a/__gcd(a,b))*b;}
#define MOD 1000000007
#define MAX 100005

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    int test;
    cin>>test;
    for(int caseno=1; caseno<=test; caseno++)
    {
        ll n;
        cin>>n;
        cout<<"Case #"<<caseno<<": ";
        ll ans,temp;
        set<int>s;
        bool flag=false;
        for(ll i=1; i<1000; i++)
        {
            temp = ans = n*i*1ll;
            while(ans>0)
            {
                s.insert(ans%10);
                ans/=10;
            }
            if(s.size()==10) {cout<<temp<<endl; flag=true; break;}
        }
        if(!flag) cout<<"INSOMNIA"<<endl;
    }
    return 0;
}
