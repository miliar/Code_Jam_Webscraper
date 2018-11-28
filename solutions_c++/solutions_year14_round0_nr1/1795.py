#include<stdio.h>
#include<string.h>
int a[5],b[5];
bool vis1[17],vis2[17];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        int r,s,ans,cnt=0;
        scanf("%d",&r);
        for(int i=1;i<=4;i++){
            if(i==r)scanf("%d%d%d%d",a+1,a+2,a+3,a+4);
            else scanf("%*d%*d%*d%*d");
        }
        scanf("%d",&s);
        for(int i=1;i<=4;i++){
            if(i==s)scanf("%d%d%d%d",b+1,b+2,b+3,b+4);
            else scanf("%*d%*d%*d%*d");
        }
        memset(vis1,0,sizeof(vis1));
        memset(vis2,0,sizeof(vis2));
        for(int i=1;i<=4;i++)vis1[a[i]]=1;
        for(int i=1;i<=4;i++)vis2[b[i]]=1;
        for(int i=1;i<=16;i++)if(vis1[i]&&vis2[i]){
            ans=i,cnt++;
        }
        if(cnt==1)printf("Case #%d: %d\n",t,ans);
        else if(cnt>1)printf("Case #%d: Bad magician!\n",t);
        else printf("Case #%d: Volunteer cheated!\n",t);
    }
    return 0;
}
