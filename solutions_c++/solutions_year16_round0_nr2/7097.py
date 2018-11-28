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
        string s;
        cin>>s;
        int a[103];
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='+') a[i]=1;
            else a[i]=0;
        }
        cout<<"Case #"<<caseno<<": ";
        int ans=0;
        int now=s.size()-1;
        while(now>=0)
        {
            if(a[now]==1) now--;
            else
            {
                ans++;
                now--;
                for(int i=now; i>=0; i--) a[i]=1-a[i];
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
