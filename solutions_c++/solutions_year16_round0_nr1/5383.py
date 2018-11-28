#include<bits/stdc++.h>
#define ll long long
#define Mod 1000000007
#define F first
#define S second
#define maxm(a,b) (a>b)?a:b
#define minm(a,b) (a<b)?a:b

using namespace std;

typedef pair< ll,ll> pii;
typedef pair<ll,pii> piii;
typedef vector<pii> vii;
ll a[121];
//map<ll,bool> visited;
bool solve(ll n)
{
    int cnt=0;
    while(n){
        a[n%10]=1;
        n/=10;
    }
    for(int i=0;i<=9;i++){
        if(a[i])
            cnt++;
    }
    if(cnt==10)
        return true;
    else
        return false;
}
int main()
{
    ll j,k,n,T,t;
    freopen("A-large.in","r",stdin);
    freopen("A-output.txt","w",stdout);
    scanf("%lld",&T);
    for(t=1;t<=T;t++){
        memset(a,0,sizeof(a));
        map<ll,bool> visited;
        ll ans=0,i=2;
        scanf("%lld",&n);
        queue< ll > q;
        q.push(n);
        while(!q.empty()){
            k=q.front();
            q.pop();
            if(visited[k]==true){
                ans=-1;
                break;
            }
            else
                visited[k]=true;
            bool sach=solve(k);
            if(sach){
                ans=k;
                break;
            }
            else{
                q.push(i*n); i++;
            }
        }
        if(ans==-1)
            printf("Case #%lld: INSOMNIA\n",t);
        else
            printf("Case #%lld: %lld\n",t,ans);
    }
    return 0;
}
