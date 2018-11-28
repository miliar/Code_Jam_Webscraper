#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<queue>
using namespace std;
#define ll long long
const int N=1000;
int pri[N+1]; //prime[0] 存的是素数的个数
void init()
{
    memset(pri,0,sizeof(pri));
    for(int i=2;i<=N;i++)
    {
        if(!pri[i]) pri[++pri[0]]=i;
        for(int j=1;j<=pri[0]&&pri[j]<=N/i;j++)
        {
            pri[pri[j]*i]=1;
            if(i%pri[j]==0) break;
        }
    }
}
int bns[20],bit[20];ll p[20];
int main()
{
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif // gh546
    init();
    int TAT; scanf("%d",&TAT);
    for(int cas=1;cas<=TAT;cas++){
        int n,num,cnt=0; scanf("%d%d",&n,&num);
        int tot=1<<(n-2);
        bit[0]=bit[n-1]=1;
        printf("Case #%d:\n",cas);
        for(int i=0;i<tot;i++){
            if(cnt==num) break;
            for(int j=0;j<n-2;j++){
                if(i&(1<<j)) bit[j+1]=1;
                else bit[j+1]=0;
            }
            int flag;
            for(int dig=2;dig<=10;dig++){
                flag=0;
                for(int k=1;k<=pri[30];k++){
                    int mod=pri[k];
                    ll tmp=1,ans=0;
                    for(int j=0;j<n;j++){
                        ans=(ans+tmp*bit[j])%mod; tmp=(tmp*dig)%mod;
                    }
                    if(ans==0){bns[dig]=mod; flag=1; break;}
                }
                if(!flag) break;
            }
            if(flag)
            {
                cnt++;
                for(int i=n-1;i>=0;i--) printf("%d",bit[i]);
                for(int i=2;i<=10;i++){
                    printf(" %d",bns[i]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}
