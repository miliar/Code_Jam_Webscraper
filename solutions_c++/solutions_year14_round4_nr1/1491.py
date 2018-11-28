#include<bits/stdc++.h>

using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define _sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful constants
#define INF                         (int)1e9
#define EPS                         1e-9

// Useful hardware instructions
#define bitcount                    __builtin_popcount

// Useful container manipulation / traversal macros
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define f                           first
#define sc                          second

#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str() // converting number (x) to string
#define SST(x) atoi(x) // converting a char array x to number

// Some common useful functions
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> pp;
typedef vector<string> VS;

#define fr(i,s,n)    for(int i=s;i<(n);++i)
#define MOD 1000000007

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

int n,x;
int a[10001];

int f(int num)
{
    int cnt=0;

    int s=0,e=n-1;

    while(s<e)
    {
        if(a[s]+a[e]<=x)
        {
            s++;
            e--;
        }
        else
        {
            e--;
        }
        cnt++;
    }

    if(s==e)cnt++;

    return (cnt<=num);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("ip.txt", "r", stdin);
    freopen("op.txt", "w", stdout);
#endif

    int T;
    cin>>T;

    for(int t=1;t<=T;++t)
    {
        cin>>n>>x;

        for(int i=0;i<n;++i)cin>>a[i];

        sort(a,a+n);

        int s=0,e=n;

        while(s<e)
        {
            int mid=(s+e)/2;
            if(f(mid))e=mid;
            else s=mid+1;
        }

        cout<<"Case #"<<t<<": "<<s<<endl;
    }

     return 0;
}

