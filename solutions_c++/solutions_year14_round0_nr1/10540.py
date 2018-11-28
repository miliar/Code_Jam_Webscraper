#include<stdlib.h>
#include<cstdio>
using namespace std;
int map[4][4];
int map2[4][4];
int ans,ans2;

void solve(int num){
    int temp[4];
    int temp2[4];
    for(int i=0;i<4;i++){
        temp[i]=map[ans-1][i];
        //printf("%d ",temp[i]);
    }
    //printf("\n");
    for(int i=0;i<4;i++){
        temp2[i]=map2[ans2-1][i];
        //printf("%d ",temp2[i]);
    }
    int cnt=0;
    int pos;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
            if(temp[i]==temp2[j]){
                pos=temp[i];
                cnt++;
            }
    }
    printf("Case #%d: ",num+1);
    if(cnt>1) printf("Bad magician!\n");
    else if(cnt==0) printf("Volunteer cheated!\n");
    else if(cnt==1) printf("%d\n",pos);
}
int main(){
    int T;
    scanf("%d",&T);
    int res=0;
    for(int w=0;w<T;w++){
        scanf("%d",&ans);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&map[i][j]);
            }
        }
        scanf("%d",&ans2);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&map2[i][j]);
            }
        }
        solve(w);
    }
}
