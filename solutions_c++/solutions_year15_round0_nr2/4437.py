#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
using namespace std;
int cnt[1010];
//int sp_time=0;
int ans=-1;
int dfs(int i,int sp_time){
    int j,l,r;
    for(i;i>0;i--)if(cnt[i]>0){
        if((sp_time+i)<ans){
            //printf("sp_time=%d i=%d\n",sp_time,i);
            ans=(sp_time+i);
        }
        for(j=2;j<=i;j++){
            if(sp_time+(j-1)*cnt[i]<ans){
                l=i%j; r=i/j; cnt[r+1]+=l; cnt[r]+=j-l;
                dfs(i-1,sp_time+cnt[i]*(j-1));
                cnt[r+1]-=l; cnt[r]-=j-l;
            }else break;
        }
        break;
    }
    return 0;
}
int main()
{
    //freopen("in2.txt","r",stdin);
    //freopen("out2.txt","w",stdout);
    int smax,n,m;

    int T,t,i,j,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d",&n);
        //cout<<n<<endl;
        k=0;
        memset(cnt,0,sizeof(cnt));
        for(i=0;i<n;i++){
            scanf("%d",&j);
            if(j>ans) ans=j;
            //cout<<j<<" ";
            cnt[j]++;
        }
       // cout<<endl;

        dfs(1000,0);
        //printf("%d\n",q.top());
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
