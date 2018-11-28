#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll unsigned long long
#define mp make_pair
#define pii pair<int,int>

vector<ll> divs;
void print(ll tmp){
    ll a = ((ll)1) << 63;
    int i=0;
    for( i=0;((a>>i & tmp)==0)&&i<63;i++);
    for(;i<=63;i++)
    {
        cout<<((a>>i & tmp)!=0);
    }
}
ll decode (ll a,ll b){
    ll ans = 0;
    ll pw = 1;
    while(a){
        ans += pw*(a & 1);
        pw*=b;
        a >>=1;
    }
    return ans ;
}
bool check(ll x,ll base)
{
    ll p = decode(x,base);
    for(int i = 2;i*i<=p;i++)
        if(p%i==0){
               // cout<<x<<" "<<p<<" "<<i<<endl;
         divs.pb(i);
                return 1;
        }
    return 0;
}
ll last = 1;
ll gen(int N){
    ll ans = ((ll)1) << (N-1);
    ll tmp = last + ans;
    do{
        divs.clear();
        bool ok = true;
        for(int i=2;i<=10;i++)
        ok &= check(tmp,i);
        last +=2;
        tmp  = last + ans ;
        if(ok)return tmp-2;
    }while(true);

}
int main()
{
    freopen("out.txt","w",stdout);
    int T=1,N,J;
    N=16;J=50;
    printf("Case #%d:\n",T);
    while(J--){
            ll a = gen(N);
            print(a);
            for(int i=0;i<9;i++)
                cout<<" "<<divs[i];
            cout<<endl;

    }
}
