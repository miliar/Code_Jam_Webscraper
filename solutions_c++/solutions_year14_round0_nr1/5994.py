#include <iostream>
#include <cstdio>
#include <vector>

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);

    int grid1[4][4],grid2[4][4];

    int t,i,j,a,b,cas = 1;

    scanf("%d",&t);

    while(t--){

        scanf("%d",&a);

        for(int i = 0;i < 4;i++){

            for(int j = 0;j < 4;j++){

                scanf("%d",&grid1[i][j]);
            }
        }
        scanf("%d",&b);

        for(int i = 0;i < 4;i++){

            for(int j = 0;j < 4;j++){

                scanf("%d",&grid2[i][j]);
            }
        }
        int count = 0,num;

        for(int i = 0;i < 4;i++){

            for(int j = 0;j < 4;j++){

                if(grid1[a-1][i] == grid2[b-1][j]){

                    count++;

                    num = grid1[a-1][i];
                }
            }
            if(count > 1){

                break;
            }
        }

        printf("Case #%d: ",cas);

        if(!count){

            printf("Volunteer cheated!\n");
        }
        else if(count == 1){

            printf("%d\n",num);
        }
        else {

            printf("Bad magician!\n");
        }
        cas++;
    }
    return 0;
}
