#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
void solve(int cnt[],int x)
{
    while(x!=0){
        cnt[x%10]++;
        x=x/10;
    }   
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output-large.in","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        int n;
        scanf("%d",&n);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        int cnt[10];
        memset(cnt,0,sizeof(cnt));
        int x=n;
        while(1){
            solve(cnt,x);
            int c=0;
            for(int i=0;i<10;i++) if(cnt[i]!=0) c++;
            if(c==10) break;
            x+=n;
        }
        printf("%d\n",x);
    }
    return 0;
}