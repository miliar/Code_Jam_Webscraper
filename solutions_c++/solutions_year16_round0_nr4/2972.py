#include <bits/stdc++.h>
#define INF 1000000000
#define mod 1000000007
#define vi vector<int>
#define vit vector<int>::iterator
#define ll long long
#define ii pair<int, int>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
using namespace std;
ll K, C, S;
static ll arr[200];
vector<ll> v;

bool solve()
{
    v.clear();
    if(C==1)
    {
        if(K>S) return false;
        for(int i=1; i<=K; i++)
            v.pb(i);
        return true;
    }
    arr[0] = 1;
    for(ll i = 1; i<=C; i++)
        arr[i] = arr[i-1]*K;
    ll pos = 0, t1 = C*arr[C-1];
    int cnt = 0, tot=0;
    for(ll i=0; tot<K && cnt<S; cnt++)
    {
        ll tmp = i*C + 1;
        ll x = 0;
        tot++;
        for(ll p = C-2; tot<K && p>=1; p--)
        {
            x += tmp*arr[p];
            tmp++;
            tot++;
        }
        if(tot==K)
        {
            x += 1;
        }
        else if(tot<K)
        {
            x += tot+1;
            tot++;
        }
        x += pos;
        v.pb(x);
        pos += t1;
    }
    if(tot<K)
        return false;
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int ctr=1; ctr<=T; ctr++)
    {
        cin>>K>>C>>S;
        if(S<K)
        {
            cout<<"Case #"<<ctr<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<"Case #"<<ctr<<": ";
        for(int i=1; i<=S; i++)
            cout<<i<<" ";
        cout<<endl;
    }
    return 0;
}
