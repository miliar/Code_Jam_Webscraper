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

const int maxn = 1000001;
bool vis[10];

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T,tCase = 0;  scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++tCase);
        int n;
        scanf("%d",&n);
        if(!n)  {printf("INSOMNIA\n");continue;}
        memset(vis,false,sizeof(vis));
        LL ans;
        bool flag;
        FOR(i,1,maxn){
            LL tem = (LL)i*n;
            ans = tem;
            while(tem)  vis[tem%10] = true,tem /= 10;   
            flag = true;
            FOR(j,0,10) if(!vis[j]) {flag = false;break;}
            if(flag)    break;
        }
        if(flag)    printf("%I64d\n",ans);
    }
    return 0;
}
