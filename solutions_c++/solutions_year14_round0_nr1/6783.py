#include<cstdio>

int a[10];
int b[10];

int main(){
    int n,i,cas,t=0,x,y,j,ans;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%d",&cas);
    while(cas--){
        scanf("%d",&x);
        for (i=1;i<=4;++i){
            if (i == x){
                for (j=0;j<4;++j)scanf("%d",&a[j]);
            }else for (j=0;j<4;++j)scanf("%d",&y);
        }
        scanf("%d",&x);
        for (i=1;i<=4;++i){
            if (i == x){
                for (j=0;j<4;++j)scanf("%d",&b[j]);
            }else for (j=0;j<4;++j)scanf("%d",&y);
        }
        ans = -1;
        for (i=0;i<4;++i){
            for (j=0;j<4;++j)if (b[i] == a[j])break;
            if (j<4){
                if(ans == -1) ans = b[i];
                else{
                    ans = -2;break;
                }
            }
        }
        printf("Case #%d: ", ++t);
        if (ans == -1) puts("Volunteer cheated!");
        else if (ans == -2) puts("Bad magician!");
        else printf("%d\n",ans);
    }
    return 0;
}
