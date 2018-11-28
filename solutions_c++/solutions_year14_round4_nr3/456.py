#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<string>
using namespace std;
struct P{
    int x,y,val;
    friend bool operator < (P a,P b){
        return a.val>b.val;
    }
};
int s[505][505],dis[505][505],dx[8]={-1,-1,-1,0,0,+1,+1,+1},dy[8]={-1,0,1,-1,1,-1,0,1};
priority_queue<P> que;
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,x,y,i,j,ans,C=0,n,m,k,a,b,c,d;
    scanf("%d",&t);
    while(t--){
        scanf("%d%d%d",&n,&m,&k);
        swap(n,m);
        memset(s,0,sizeof(s));
        for(i=0;i<k;i++){
            scanf("%d%d%d%d",&a,&b,&c,&d);
            swap(a,b);
            swap(c,d);
            for(x=a;x<=c;x++)
            for(y=b;y<=d;y++){
                s[x][y]=1;
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++)
                dis[i][j]=99999999;
        }
        for(i=0;i<n;i++){
            que.push((P){i,0,1-s[i][0]});
            dis[i][0]=1-s[i][0];
        }
        int ans=-1;
        while(que.size()){
            P vv=que.top();
            que.pop();
            //printf("(%d.%d.)\n",vv.x,vv.y);
            x=vv.x,y=vv.y;
            if(vv.y==m-1){
                if(ans==-1 || vv.val<ans) ans=vv.val;
                continue;
            }
            for(i=0;i<8;i++){
                int X=x+dx[i],Y=y+dy[i];
                if(X<n && X>=0 && Y<m && Y>=0){
                    if(vv.val+1-s[X][Y]<dis[X][Y]){
                        dis[X][Y]=vv.val+1-s[X][Y];
                        que.push((P){X,Y,dis[X][Y]});
                    }
                }
            }
            //printf("%d,,,",que.size());
        }
        /*for(i=0;i<n;i++){
            for(j=0;j<m;j++)
                printf("%d ",dis[i][j]);
            puts("");
        }*/
        printf("Case #%d: %d\n",++C,ans);
    }
}
