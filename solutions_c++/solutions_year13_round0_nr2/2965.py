#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int grid[110][110];
int mow[110][2];

int main(){
    int i,j;
    int t,T;
    int R,C;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        memset(mow,-1,sizeof mow);
        printf("Case #%d: ",t);
        scanf("%d%d",&R,&C);
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                scanf("%d",&grid[i][j]);
            }
        }
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                mow[i][0]=max(mow[i][0],grid[i][j]);
                mow[j][1]=max(mow[j][1],grid[i][j]);
            }
        }
        bool flag=true;
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                if(grid[i][j]!=min(mow[i][0],mow[j][1])){flag=false;break;}
            }
            if(!flag)break;
        }
        if(flag)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
