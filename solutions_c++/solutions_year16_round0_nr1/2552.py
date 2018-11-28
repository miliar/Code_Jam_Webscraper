//created by shikhar vishnoi

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <math.h>
#define ll long long
#define pb push_back
#define iosync ios_base::sync_with_stdio(false);cin.tie(0);
const ll mod=1000000007;
const double pi=3.14159265358979323846;
using namespace std;

ll solve (ll n)
{
    ll mask=0,x=1;
    while(mask != (1<<10)-1)
    {
        ll tmp = n*x;
        while(tmp)
        {
            mask |= (1<<(tmp%10));
            tmp /= 10;
        }
        x++;
    }
    return (n*(x-1));
}

int main ()
{
    
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    iosync
    ll T;
    cin>>T;
    for(ll t=1; t<=T; t++)
    {
        ll n;
        cin>>n;
        if(n)
            cout<<"Case #"<<t<<": "<<solve(n)<<endl;
        else
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    return 0;
}