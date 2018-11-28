#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define read() freopen("in.txt","r",stdin)
#define arrsize (int)1e6+1
#define vul()  printf("-1\n");
#define out() cout<<ans<<endl;
#define loop(i,n) for( int i =0; i<n; i++)
#define loopn(i,n) for( int i=1; i<=n; i++)
#define debug1(x) cout<<x<<endl;
#define debug2(x,y) cout<<x<<ends<<y<<endl;
#define debug3(x,y,z) cout<<x<<ends<<y<<ends<<z<<endl;
#define sdi(x) cin>>x;
#define sdii(x,y) cin>>x>>y;
#define YES cout<<"yes\n";
#define NO cout<<"no\n";
#define newline cout<<endl
#define MEM(arr, value) memset( arr, value , sizeof arr)

int Set( int n, int pos)
{
    return ( n=n | 1<<pos );
}
int reset(int N,int pos)
{
    return N= N & ~(1<<pos);
}
bool check(int N,int pos)
{
    return (bool)(N & (1<<pos));
}
ll pow(ll a, ll b, ll mod)
{
    ll x = 1, y = a;
    while(b > 0)
    {
        if(b%2 == 1)
        {
            x=(x*y);
            if(x>mod) x%=mod;
        }
        y = (y*y);
        if(y>mod) y%=mod;
        b /= 2;
    }
    return x;
}

ll modInverse(ll a, ll m)
{
    return pow(a,m-2,m);
}

ll mod = 1e9+7;


int main()
{
    read();
    freopen("out.txt", "w", stdout);

    int test, kase=1;
    cin>>test;
    ll j;
    while(test--)
    {
        int n;
        cin>>n;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n", kase++);
            continue;
        }
        ll ans ;
        int tot[11]= {};
        MEM(tot, 0);
        for(  j = 1; ; j++)
        {
            ll temp = n*j;
            ans = temp;
//           cout<<temp<<endl;
            while( temp)
            {
                tot[temp%10]++;
                temp/=10;
            }
            int k ;
            for(  k =0; k<=9; k++)
            {
                if(tot[k]==0)
                {
//                    cout<<k<<endl;
                    break;
                }
            }
            if(k==10)
            {
                break;
            }

        }


        printf("Case #%d: %lld\n",kase++,ans );
    }


}
