/*--------------------------
|  Author- Advitiya Brijesh |
|  PIE @ MNNIT Allahabad    |
|  advitiyabrijesh@gmail.com|
|                           |
---------------------------*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<list<ll> > vli;
typedef vector<int> vi;
typedef vector<pair<ll,ll> > vpll;
typedef vector<pair<int,int> > vpii;
typedef pair<int ,int> pii;
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,a,b) for(int i=a;i<=b;++i)
#define PER(i,b) for(int i=b;i>=0;--i)
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define ss(n) scanf("%s",n)
#define sc(n) scanf("%c",&n)
#define oll(n) printf("%lld\n",n);
#define mset(n,k) memset(n,k,sizeof(n))
#define MOD 1000000007
#define MAX 2000005
#define MAXN 100005
int dp[1000005];
int main(){
    freopen("lucky.in","r",stdin);
    freopen("lucky.out","w",stdout);
    
    int t;
    sd(t);
    ll idx;
    dp[0]=-1;
    for(ll i=1;i<=1000000;++i){
        int has[10]={0};
        ll tmp=i,val,temp,ans;
        for(val=1;;val++){
            temp=val*tmp;
            ans=temp;
            while(temp){
                has[temp%10]=1;
                temp/=10;
            }
            int j;
            for(j=0;j<10;++j){
                if(!has[j])
                    break;
            }
            if(j==10)
                break;
        }
        if(ans<val){
            ans=val;
            idx=i;
        }
        dp[i]=ans;
    }
    //cout<<mxn<<endl;
    //cout<<ans<<" "<<idx<<endl;
    for(int tc=1;tc<=t;++tc){
        int n;
        sd(n);
        if(n>0)
        printf("Case #%d: %d\n",tc,dp[n]);
        else
        printf("Case #%d: INSOMNIA\n",tc);
    }
return 0;}