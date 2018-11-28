#include<cstdio>
int a,b,c;
int main(){
    int t,n,m,cnt;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        scanf("%d %d",&n,&m);
        printf("Case #%d:\n",turn);
        for(int i=0;i<m;i++){
            printf("11");
            for(int j=0;j<(n/2)-2;j++){
                if(i&(1<<j)) printf("11");
                else printf("00");
            }
            printf("11");
            for(int j=3;j<=11;j++) printf(" %d",j);
            printf("\n");
        }
    }
}
