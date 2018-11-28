#include <cstdio>

int main()
{
    int t, f, r1, r2, num, c = 0;
    int g1[4][4], g2[4][4];
    int v[4];
    scanf("%d",&t);

    while(t)
    {
        c++;
        scanf("%d",&r1);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d",&g1[i][j]);
        for(int i = 0; i < 4; i++)
            v[i] = g1[r1-1][i];
        scanf("%d",&r2);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d",&g2[i][j]);
        f = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(g2[r2-1][i] == v[j]){
                    if(!f){
                        f = 1;
                        num = v[j];
                    }
                    else f = 2;
                }
            }
        }
        printf("Case #%d: ",c);
        if(f == 0) printf("Volunteer cheated!\n");
        else if(f == 1) printf("%d\n",num);
        else if(f == 2) printf("Bad magician!\n");


        t--;
    }

}
