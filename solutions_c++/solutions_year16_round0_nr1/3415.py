#include<bits/stdc++.h>
#define ll long long
#define fi first
#define se second
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
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
bool a[10];
void solve(){
    int n;
    cin>>n;
    if(n==0){
        cout<<"INSOMNIA"<<endl;
        return;
    }
    int max1=-1;
    mem(a,false);
    for(int j=1;j<=100;j++){
            int k=j*n;
            while(k){
            a[k%10]=1;
            k/=10;
            }
            int f=1;
            for(int i=0;i<10;i++){
                if(a[i]!=1){
                    f=0;
                    break;
                }
            }
            if(f){
               max1=max(max1,j);
               break;
            }
        }
    cout<<max1*n<<endl;
}
int main(){
   //ios_base::sync_with_stdio(false);
   freopen("input.IN","r",stdin);
   freopen("out.txt","w",stdout);
   int t=1;
   sd(t);
   for(int i=1;i<=t;i++){
       printf("Case #%d: ",i);
       solve();
   }
   return 0;
}
