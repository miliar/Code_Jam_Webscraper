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

ll isprime (ll num)
{
    ll factor=0,sq=sqrt(num)+1;
    for (int i = 2; i <= sq; ++i)
    {
        if(num%i == 0)
            {factor=i;break;}
    }
    return factor;
}

ll calc (string s)
{
    ll factor[11];
    reverse(s.begin(),s.end());
    for (int i = 2; i < 11; ++i)
    {
        ll num=0,tmp;
        for (int j = 0; j < s.size(); ++j)
            if(s[j] == '1')
                num += pow(i,j);
        tmp=isprime(num);
        if(tmp==0)
            return 0;
        else
            factor[i]=tmp;
    }
    reverse(s.begin(),s.end());
    cout<<s;
    for (int i = 2; i < 11; ++i)
        cout<<" "<<factor[i];
    cout<<endl;
    return 1;
}

void solve (ll n,ll j)
{
    for (int mask = 0; mask < (1<<(n-2)); ++mask)
    {
        string s="1";
        for (int i = 0; i < (n-2); ++i)
        {
            if(mask & (1<<i))
                s += '1';
            else
                s += '0';
        }
        s += '1';
        if(j)
            j -= calc(s);
        else
            break;
    }
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
        ll n,j;
        cin>>n>>j;
        cout<<"Case #"<<t<<": "<<endl;
        solve(n,j);
    }
    return 0;
}