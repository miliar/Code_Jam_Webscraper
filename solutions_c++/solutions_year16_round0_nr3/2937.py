#include<bits/stdc++.h>
#define ll long long
#define fi first
#define se second
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}
ll nmpow(ll a, ll n)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b);b=(b*b);n>>=1;}
return (ll)ret;
}
using namespace std;
#define mem(x,a) memset(x,a,sizeof(x))
#define pii pair<int,int>
#define sd(x) scanf("%d",&x)
#define pd(x) printf("%d",x)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define N (int)1e6+4
using namespace std;
long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
ll modulo(ll a,ll b,ll c){
    long long x=1,y=a;
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c;
        b /= 2;
    }
    return x%c;
}
bool Miller_Rabin(ll val,int x){
    if(val<2)
        return false;
    if(val!=2&&val%2==0){
        return false;
    }
    ll nx=val-1;
    while(nx%2==0){
        nx/=2;
    }
    for(int i=0;i<x;i++){
        ll a=rand()%(val-1)+1,temp=nx;
        ll mod=modulo(a,temp,val);
        while(temp!=val-1&&mod!=1&&mod!=val-1){
            mod=mulmod(mod,mod,val);
            temp*=2ll;
        }
        if(mod!=val-1&&temp%2==0){
            return false;
        }
    }
    return true;
}
void solve(){
    int n=16;
    vector<int> ans;
    for(int i=2;i<(1<<n);i++){
        if(!(i&(1<<(15))))
            continue;
        if(!(i&(1<<(0))))
            continue;
        int f=1;
        for(ll base=2;base<=10;base++){
            ll num=0;
            for(int j=15;j>=0;j--){
                if(i&(1<<j)){
                    num+=nmpow(base,j);
                }
            }
            if(Miller_Rabin(num,20)){
               f=0;
               break;
            }
        }
        if(f){
           ans.pb(i);
           if(ans.size()==100)
                break;
        }
    }
    int tot=0;
    for(int i=0;i<ans.size();i++){
        string x;
        int k=ans[i];
        while(k){
            x+=(k%2+'0');
            k/=2;
        }
        reverse(x.begin(),x.end());
        vector<int> div;
        int cnt=0;
        for(ll base=2;base<=10;base++){
            ll num=0;
            for(int j=15;j>=0;j--){
                if(ans[i]&(1<<j)){
                    num+=nmpow(base,j);
                }
            }
            for(int p=2;p<=sqrt(num);p++){
                if(num%p==0){
                    cnt++;
                    div.pb(p);
                    break;
                }
            }
        }
        if(cnt==9){
           cout<<x<<" ";
           for(int i=0;i<div.size();i++){
               cout<<div[i]<<" ";
           }
           cout<<endl;
           tot++;
           if(tot==50)
            break;
        }
    }
}
int main(){
   //ios_base::sync_with_stdio(false);
   freopen("input.IN","r",stdin);
   freopen("out.txt","w",stdout);
   int t=1;
   sd(t);
   for(int i=1;i<=t;i++){
       printf("Case #%d: \n",i);
       solve();
   }
   return 0;
}
