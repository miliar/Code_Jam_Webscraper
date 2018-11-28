#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
    int index,icase=0;
    int arr[55][55];
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&index);
    while(index--){
        int k;
        printf("Case #%d:\n",++icase);
        memset(arr,0,sizeof(arr));
        int x,y;
        scanf("%d%d%d",&x,&y,&k);
        int t=x*y-k;
        int res=1;
        int n=min(x,y);
        int m=max(x,y);
        if (t==1){
            res=1;
        }else if (n==2){
            if ((t&1)||t<4)res=0;
            else{
                for (int i=0;i<t;i++)
                    if (x<y)arr[i%n][i/n]=1;
                    else arr[i/n][i%n]=1;
            }
        }else if (n==1){
            if (t<=1)res=0;
            else{
                for (int i=0;i<t;i++)
                    if (x<y)arr[i%n][i/n]=1;
                    else arr[i/n][i%n]=1;
            }
        }else{
             if (t<4||t==5||t==7)res=0;
             else{
                int i=n;
                for (;i>=2;i--)
                    if (t/i>=2)break;
                for (int j=0;j<t;j++)
                    if (x<y)arr[j%i][j/i]=1;
                    else arr[j/i][j%i]=1;
                if (t%i==1)
                    if (x<y){
                        arr[(t)%i][(t)/i]=1;
                        arr[i-1][(t)/i-1]=0;
                        if ((t)/i-1==1){
                            arr[(t+1)%i][(t+1)/i]=1;
                            arr[i-1][(t)/i-2]=0;
                        }
                    }else{
                        arr[(t)/i][(t)%i]=1;
                        arr[t/i-1][i-1]=0;
                        if ((t)/i-1==1){
                            arr[(t+1)/i][(t+1)%i]=1;
                            arr[t/i-2][i-1]=0;
                        }
                    }
             }
        }
        if (res<=0){
            puts("Impossible");
            continue;
        }
        arr[0][0]=-1;
        for (int i=0;i<x;i++){
            for (int j=0;j<y;j++){
                if (arr[i][j]==-1)printf("c");
                if (arr[i][j]==0)printf("*");
                if (arr[i][j]==1)printf(".");
            }
            puts("");
        }
    }
    return 0;
}
