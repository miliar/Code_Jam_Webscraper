/*
    Author:- Deepak Singh Mehta.

    Deciding what not to do is
    as impotant as deciding
    what to do.



*/


#include<bits/stdc++.h>
#define pb push_back
#define p(a) pair<int,int>
#define mp make_pair
#define NAX 1001
#define MOD 1000000007
#define v(a) vector<int>
#define fastio ios::sync_with_stdio(false)
#define si(a) scanf("%d",&a)
#define ll long long
#define ff first
#define ss second
using namespace std;
int main(){
    //fastio;
    ll tests;
    cin>>tests;
    for(ll c=1;c<=tests;++c){
        ll n;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<c<<": INSOMNIA"<<endl;
            continue;
        }
        set<ll> dig;
        ll ans;
        bool flag=false;
        for(ll i=1;;i++){
            ll m=n*i;
            ll res=m;
            while(m){
                int rem=m%10;
                dig.insert(rem);
                m/=10;
                if(dig.size()==10){
                    flag = true;
                    ans = res;
                    break;
                }
            }
            if(flag)break;
        }
        cout<<"Case #"<<c<<": "<<ans<<endl;

    }

    return 0;
}
