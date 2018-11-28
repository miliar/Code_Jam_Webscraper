#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

typedef unsigned long long LL;
int S=10000;

LL modular_multi(LL x,LL y,LL mo)
{
    LL t;
    x%=mo;
    for(t=0;y;x=(x<<1)%mo,y>>=1)
        if (y&1)
            t=(t+x)%mo;
    return t;
}

LL modular_exp(LL num,LL t,LL mo)
{
    LL ret=1,temp=num%mo;
    for(;t;t>>=1,temp=modular_multi(temp,temp,mo))
        if (t&1)
            ret=modular_multi(ret,temp,mo);
    return ret;
}

bool miller_rabbin(LL n)
{
    if (n==2)return true;
    if (n<2||!(n&1))return false;
    int t=0;
    LL a,x,y,u=n-1;
    while((u&1)==0) t++,u>>=1;
    for(int i=0;i<S;i++)
    {
        a=rand()%(n-1)+1;
        x=modular_exp(a,u,n);
        for(int j=0;j<t;j++)
        {
            y=modular_multi(x,x,n);
            if (y==1&&x!=1&&x!=n-1)
                return false;
            ///其中用到定理，如果对模n存在1的非平凡平方根，则n是合数。
            ///如果一个数x满足方程x^2≡1 (mod n),但x不等于对模n来说1的两个‘平凡’平方根：1或-1，则x是对模n来说1的非平凡平方根
            x=y;
        }
        if (x!=1)///根据费马小定理,若n是素数，有a^(n-1)≡1(mod n).因此n不可能是素数
            return false;
    }
    return true;
}

LL a[15];
LL num[15][20];

LL prime[1000005];
int vis[1000005];
int cnt;
int n,m;

void init(){
    cnt=0;
    memset(vis,0,sizeof(vis));
    for(LL i=2;i<=100000;i++){
        if(!vis[i]){
            prime[cnt++]=i;
            for(int j=i;j<=1000000;j+=i){
                vis[j]=1;
            }
        }
    }
    for(LL i=2;i<=10;i++){
        num[i][1]=i;
        for(int j=2;j<=16;j++){
            num[i][j]=num[i][j-1]*i;
        }
    }
}

LL getyz(LL x){
    for(int i=0;i<cnt;i++){
        if(x%prime[i]==0) return prime[i];
    }
    return 0;
}

LL getnum(int s,int p){
    LL ans=num[p][n-1]+1;
    for(int i=0;i<n-2;i++){
        if((1<<i)&s){
            ans+=num[p][i+1];
        }
    }
    return ans;
}

int tt[55][20];
LL res[55][15];

void print_num(int s,int id){
    tt[id][1]=1;
    tt[id][n]=1;
    for(int i=0;i<n-2;i++){
        if((1<<i)&s){
            tt[id][i+2]=1;
        }
        else{
            tt[id][i+2]=0;
        }
    }
    /*for(int i=n;i>=1;i--){
        printf("%d",tt[id][i]);
    }*/
}

int main(){
    //freopen("c.in","r",stdin);
    //freopen("c.out","w",stdout);
    int T,ca=0;
    int i,j;
    init();
    scanf("%d",&T);
    while(T--){
        ca++;
        scanf("%d%d",&n,&m);
        int cc=0;
        int len=n-2;
        for(i=0;i<(1<<len);i++){
            memset(a,0,sizeof(a));
            for(j=2;j<=10;j++){
                LL t=getnum(i,j);
                if(miller_rabbin(t)) break;
                a[j]= getyz(t);
                if(a[j]==0)break;
            }
            if(j>10){
                print_num(i,cc);
                for(j=2;j<=10;j++){
                    res[cc][j]=a[j];
                }
                cc++;
                if(cc==m) break;
            }
        }
        printf("Case #%d:\n",ca);
        for(i=0;i<m;i++){
            for(j=n;j>=1;j--){
                printf("%d",tt[i][j]);
            }
            for(j=2;j<=10;j++){
                cout<<" "<<res[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}
