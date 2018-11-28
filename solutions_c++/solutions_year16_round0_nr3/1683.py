#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int ans[11];
int bits[33];

bool divisible(int n, int x, int v){
    int mod = 0;
    for(int i=n-1; i>=0; --i){
        mod = mod * x + bits[i];
        mod %= v;
    }
    return mod==0;
}

bool check(int num, int n){
    bits[0]=bits[n-1]=1;
    int p=1;
    while(num){
        bits[p++]=num%2;
        num/=2;
    }
    for(int x=2; x<=10; ++x){
        bool found = 0;
        for(int v=2; v<=300; ++v)
            if(divisible(n, x, v)){
                found = 1;
                ans[x] = v;
                break;
            }
        if(!found) return 0;
    }

    return 1;
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,n,j;
    scanf("%d%d%d",&T,&n,&j);
    printf("Case #1:\n");
    for(int v=0; j>0 && v<(1<<(n-2)); ++v){
        if(check(v,n)){
            for(int i=n-1; i>=0; --i) printf("%d",bits[i]);
            for(int i=2; i<=10; ++i) printf(" %d",ans[i]);
            puts("");
            --j;
        }
    }
}

