/*
    xxx_joker/codersumit
*/
#include<bits/stdc++.h>
#define bitcnt(x) __builtin_popcountll(x)
#define sd(a) scanf("%d",&a)
#define sld(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define sc(a) scanf("%c",&a)
#define pd(a) printf("%d",a)
#define ps(a) printf("%s",a)
#define pc(a) printf("%c",a)
#define space printf(" ");
#define nw printf("\n")
#define pb push_back
#define FOR(i,a,b) for(i=a;i<b;i++)
#define FORR(i,a,b) for(i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define MAX 1000005
#define inf 1e8
#define mod 1000000007

typedef long long ll;
typedef unsigned long long ull;
using namespace std;
int dvisit[11],visit[MAX];
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int temp,m,test,n,i,cnt,flag,k;
    sd(test);
    FOR(k,1,test+1){
        memset(visit,0,sizeof(visit));
        memset(dvisit,0,sizeof(dvisit));
        flag=0;
        sd(m);
        n=m;
        while(!flag){
            cnt=0;
            FOR(i,0,11){
                if(dvisit[i])
                    cnt++;
            }
            if(cnt>=10)
                flag=1;
            if(visit[n]==1)
                flag=2;
            temp=n;
            visit[temp]=1;
            while(temp>0){
                dvisit[temp%10]=1;
                temp/=10;
            }
            n+=m;
        }
        if(flag==2)
            printf("Case #%d: INSOMNIA\n",k);
        else
            printf("Case #%d: %d\n",k,(n-(m+m)));
    }
    return 0;
}
