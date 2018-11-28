/* Author: vishparekh */

#include<bits/stdc++.h>
using namespace std;

#define FOR(i,start,stop,step) for(ll i=start; i<stop; i+=step)
#define fore(it,v) for(it=v.begin(); it!=v.end(); it++)
#define SZ(V) (int)V.size()
#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define fi first
#define se second
#define Pi 3.14159265358979

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> V;
typedef pair<int, int> PII;

const int INF_MAX = 2147483647;
const int INF_MIN = -2147483647;
const int MOD =  1000000007;

bool check(ll n,int a[])
{
    ll sum = 0;
    while(n!=0)
    {
        int b = n % 10;
        if(b == 0)
            a[0] = 1;
        else if(b == 1)
            a[1] = 1;
        else if(b == 2)
            a[2] = 1;
        else if(b == 3)
            a[3] = 1;
        else if(b == 4)
            a[4] = 1;
        else if(b == 5)
            a[5] = 1;
        else if(b == 6)
            a[6] = 1;
        else if(b == 7)
            a[7] = 1;
        else if(b == 8)
            a[8] = 1;
        else if(b == 9)
            a[9] = 1;

        n = n/10;
    }
    for(int i = 0 ; i < 10 ; i++ )
    {
        //cout<<a[i]<<" ";
        sum = sum + a[i];
    }
    //cout<<endl;
    if(sum == 10)
        return true;
    else
        return false;

}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    ll i = 1;
    while(t--)
    {

        ll ans;
        ll n;
        ll m = 1;
        int a[10]={0};
        cin>>n;
        if(n != 0)
        {
            while(!check(n*m,a))
            {
                m++;
            }
            cout<<"Case #"<<i<<": "<<m*n<<endl;
            i++;
        }
        else
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            i++;
        }

    }

    return 0;
}
