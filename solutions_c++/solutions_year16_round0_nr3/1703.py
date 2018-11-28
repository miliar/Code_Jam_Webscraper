#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair <int,int>  PII;
#define FOR(i,x,y)  for(int i = x;i < y;++ i)
#define IFOR(i,x,y) for(int i = x;i > y;-- i)
#define pb  push_back
#define mp  make_pair
#define fi  first
#define se  second

const int maxn = 1000;
bool check[maxn];
int prime[maxn];

void Mobius(){
    memset(check,false,sizeof(check));
    prime[0] = 0;
    FOR(i,2,maxn){
        if(!check[i])  prime[++prime[0]] = i;
        FOR(j,1,prime[0]+1){
            if(i*prime[j] > maxn)   break;
            check[i*prime[j]] = true;
            if(i % prime[j] == 0)  break;
        }
    }
}

int n,J;

int judge(LL num,int base){
    int ans = 0;
    FOR(i,1,prime[0]+1){
        int rmd = 0;
        LL t = num;
        int dv = 1;
        while(t){
            rmd = (dv*(t%2)+rmd)%prime[i];
            t >>= 1;
            dv = dv*base%prime[i];
        }
        if(rmd == 0) {ans = prime[i];break;}
    }
    return ans;
}

int bit[32],a[10];

void work(){
    LL st = (1LL<<(n-1))|1;
    LL en = (1LL<<n)-1;
    for(LL i = st;i <= en;i += 2){
        bool f = true;
        FOR(j,2,11){
            int t = judge(i,j);
            if(!t) {f = false;break;}
            a[j] = t;
        }
        if(!f)  continue;
        LL num = i;
        int sz = 0;
        while(num)  bit[sz++] = num%2,num >>= 1; 
        IFOR(j,sz-1,-1) printf("%d",bit[j]);
        FOR(j,2,11) printf(" %d",a[j]);
        printf("\n");
        J--;
        if(!J || i == en)  break;
    }
}

int main(){
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    Mobius();
    int T,tCase = 0;  scanf("%d",&T);
    while(T--){
        printf("Case #%d:\n",++tCase);
        scanf("%d%d",&n,&J);
        work();
    }
    return 0;
}
