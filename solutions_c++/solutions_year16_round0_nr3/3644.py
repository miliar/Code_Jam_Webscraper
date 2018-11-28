#include<bits/stdc++.h>
using namespace std;

typedef __int64 ll;

int n,k;
int ans;
int judge(int x,int t) {
    ll tmp=1,p=0;
    for(int i=0;i<n;i++) {
        if((1<<i)&x) p+=tmp;
        tmp*=t;
    }
    for(ll i=2;i*i<=p;i++) if(p%i==0) return i;
    return 0;
}
void dfs(int cnt,int x) {
    if(ans==k) return ;
    if(cnt==n-1) {
        int g[11],t=0;
        for(int i=2;i<=10;i++) {
            int r=judge(x,i);
            if(r) g[t++]=r;
            else return ;
        }
        for(int i=n-1;i>=0;i--) if((1<<i)&x) printf("1");else printf("0");
        for(int i=0;i<9;i++) printf(" %d",g[i]);
        puts("");
        ans++;
        return ;
    }
    dfs(cnt+1,x+(1<<cnt));
    dfs(cnt+1,x);
}
int main() {
    freopen("C-small-attempt1.in","r",stdin);
    freopen("text.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++) {
        scanf("%d%d",&n,&k);
       // printf("WW %d %d\n",n,k);
        printf("Case #%d:\n",ca);
        int t=1+(1<<(n-1));
        dfs(1,t);
    }
    return 0;
}
