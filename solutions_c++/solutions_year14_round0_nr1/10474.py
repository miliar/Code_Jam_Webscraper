#include<cstdio>

using namespace std;

int main(){
    //freopen("A-small-attempt0 (1).in","r",stdin);
    //freopen("output.in","w",stdout);
    int tc;
    scanf("%d",&tc);
    int a,b,hasil,temporer;
    int c[4][4],d[4][4];
    for(int i=1;i<=tc;i++){
        hasil=0,temporer=0;
        scanf("%d",&a);
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++)
                scanf("%d",&c[j][k]);
        }
        scanf("%d",&b);
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++)
                scanf("%d",&d[j][k]);
        }
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(c[a-1][j]==d[b-1][k]){
                    hasil++;
                    temporer=c[a-1][j];
                }
            }
        }
        if(hasil==1) printf("Case #%d: %d\n",i,temporer);
        else if(hasil>1) printf("Case #%d: Bad magician!\n",i);
        else printf("Case #%d: Volunteer cheated!\n",i);
    }
}
