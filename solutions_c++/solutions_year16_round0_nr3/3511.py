#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>
using namespace std;

typedef long long ll;
vector<int>prime;
vector<int> v;
int vis[1000005];
int a[35];

void get_prime(){
    memset(vis,0,sizeof(vis));
    prime.clear();
    for(int i = 2; i <= 1000000; i++){
        int tt = 1000000/i;
        for(int j = 2; j <= tt; j++)
            vis[i*j] = 1;
    }
    for(int i = 2; i <= 1000000; i++){
        if(!vis[i])
            prime.push_back(i);
    }
}

int check(ll ans){
    int len = prime.size();
    for(int i = 0; i < len && (ll)prime[i]*prime[i] <= ans; ++i){
        if(ans%prime[i] == 0)
            return prime[i];
    }
    return -1;
}

int change(ll x,int base){
    ll ans = 0;
    int cnt = 0;
    while(x){
        a[cnt++] = x%2;
        x /= 2;
    }
    for(int i = cnt-1; i >= 0; --i)
        ans = ans*base+a[i];
    //cout<<ans<<endl;
    return check(ans);
}

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    get_prime();
    int T,t = 0;
    scanf("%d",&T);
    while(T--){
        int n,j,x,cnt = 0;
        scanf("%d%d",&n,&j);
        printf("Case #%d:\n",++t);
        ll sum = 1LL<<n;
        for(ll i = (1LL<<(n-1))+1; i < sum && j; i += 2){
            //cout<<i<<endl;
            int flag = 1;
            v.clear();
            for(int k = 2; k <= 10; ++k){
                x = change(i,k);
                if(x == -1){
                    flag = 0;
                    break;
                }
                v.push_back(x);
            }
            if(flag){
                --j;
                x = i;
                int cnt = 0;
                while(x){
                    a[cnt++] = x%2;
                    x /= 2;
                }
                for(int k = cnt-1; k >= 0; --k)
                    printf("%d",a[k]);
                for(int k = 0; k < 9; ++k)
                    printf("% d",v[k]);
                printf("\n");
            }
        }
    }
    return 0;
}
