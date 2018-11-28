#include<bits/stdc++.h>
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define eb emplace_back
#define pb push_back
#define ll long long
#define mp make_pair
#define x first
#define y second
#define mod 1000000007
#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b
using namespace std;
ll solve()
{
    ll n;
    cin >> n;
    if(n==0)
        return -1;
    else
    {
        int cnt[10]={0};
        ll i;ll a;ll curr;ll ans;
        i=1;int c=0;
        while(1)
        {
            curr=i*n;
            ans=curr;
            while(curr>0)
            {
                a=curr%10;
                if(cnt[a]==0){
                    cnt[a]++;c++;
                }
                curr/=10;
            }
            i++;
            if(c==10)
                break;
        }
        return ans;
    }
}
int main()
{
        int t;
    cin >> t;
    int j;
    rep(j,0,t)
    {
        ll k=solve();
        if(k==-1)
            cout << "Case #" << j+1 << ": " << "INSOMNIA\n";
        else
             cout << "Case #" << j+1 << ": " << k << "\n";
    }
    return 0;
}