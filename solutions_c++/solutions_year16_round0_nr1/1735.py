#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define s second
#define ll long long
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
int func(ll num){
    int mask=0;
    while(num>0){
        mask|=(1<<(num%10));
        num/=10;
    }
    return mask;
}
int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("output1.txt","w",stdout);

    int T;
    cin >> T;
    int cur=1;
    while(T--){
        ll N;
        cin >> N;
        cout<<"Case #"<<cur<<": ";
        cur++;
        if(N==0){
            cout<<"INSOMNIA\n";
            continue;
        }
        ll now=N;
        int mask=0;
        while(1){
            mask|=func(now);
            if(mask==(1<<10)-1){
                break;
            }
            now+=N;
        }
        cout<<now<<"\n";

    }
}
