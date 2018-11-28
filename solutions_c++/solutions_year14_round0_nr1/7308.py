#include "iostream"
#include "cstdio"

using namespace std;

int main(){
    int t,grid1[4][4],grid2[4][4],ans1,ans2,c,save;
    scanf("%d",&t);
    for(int d=0;d<t;d++){
        scanf("%d",&ans1);
        ans1--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&grid1[i][j]);
        scanf("%d",&ans2);
        ans2--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&grid2[i][j]);
        c=0,save=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                //cout<<"BLADF\n";
                if(grid1[ans1][i]==grid2[ans2][j]/*||grid1[ans1][j]==grid2[ans2][i]*/){
                    //printf("Entering here\n");
                    c++;
                    save=grid1[ans1][i];
                }
            }
        }
        printf("Case #%d: ",d+1);
        if(c==0)
            printf("Volunteer cheated!\n");
        else if(c==1)
            printf("%d\n",save);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
