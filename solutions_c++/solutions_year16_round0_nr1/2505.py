#include <bits/stdc++.h>

typedef long long LL;
typedef unsigned long long ULL;
typedef long double ld;
typedef __float128 bfl;

const int MOD = 1000000007;

#define f first
#define s second
#define pll pair<LL, LL> 
#define pii pair<int, int> 
#define mp make_pair
#define pb push_back
#define SC static_cast

using namespace std;

int x, t, i;
const LL full_mask = (1<<10)-1;

LL pick_digits(LL x)
{
    LL res = 0;
    do
    {
        res|=1<<(x%10);
        x/=10;
    }
    while (x);
    return res;
}
void solve()
{
    cin>>x;

    cout<<"Case #"<<i+1<<": ";
    if(x)
    {
        LL bit_mask = 0,
           tmp = x;
        while ((bit_mask|=pick_digits(tmp))!=full_mask) tmp+=x;
        cout<<tmp<<endl;        
    }
    else 
        cout<<"INSOMNIA\n";

}

int main()
{
    cin>>t;
    for( i = 0; i<t; i++ )
        solve();
    return 0;
}
