#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

int vis[1010],x[1010];
int check(int m,int z){
    memcpy(x,vis,sizeof vis);
    int l=1,r=z;
    while(l<r){
        int mid=l+r>>1;
        int ans=0;
        for(int i=mid+1;i<=z;i++)
            if(x[i]) ans+=((i+mid-1)/mid-1)*x[i];
        //cout<<ans<<" "<<l<<" "<<r<<" "<<endl;
        if(ans>m) l=mid+1;
        else r=mid;
    }
    return l;
}
int main()
{
    //freopen("1.txt","r",stdin);
    //freopen("2.txt","w",stdout);
    int t,d,p,r,cas=1;
    scanf("%d",&t);
    while(t--){
        r=0;
        memset(vis,0,sizeof vis);
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            scanf("%d",&p);
            vis[p]++;
            r=max(r,p);
        }
        int ans=r;
        //cout<<vis[3]<<"***"<<endl;
        for(int i=0;i<=r;i++){
            //cout<<check(i,r)<<"***"<<endl;
            //if(i==0) cout<<check(i,r)<<endl;
            ans=min(ans,i+check(i,r));
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
	return 0;
}
