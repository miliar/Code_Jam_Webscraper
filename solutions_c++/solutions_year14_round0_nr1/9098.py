#include <cstdio>

int main()
{
    FILE *p, *out;
    p=fopen("A-small-attempt0.in", "r");
    out = fopen("output.txt", "w");

    int n_teste, ind=1;
    fscanf(p, "%d", &n_teste);

    while(ind<=n_teste)
    {
        int card[5][5];
        int choose[5], ans;

        int a;
        fscanf(p, "%d", &a);
        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
            fscanf(p, "%d", &card[i][j]);
        for(int i=1; i<=4; i++)
            choose[i]=card[a][i];

        fscanf(p, "%d", &a);
        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
            fscanf(p, "%d", &card[i][j]);

        int cont=0;
        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
            if(choose[j]==card[a][i])
                ans=choose[j], cont++;

        if(cont==1)
            //printf("Case #%d: %d\n", ind++, ans);
            fprintf(out, "Case #%d: %d\n", ind++, ans);
        if(cont>1)
            //printf("Case #%d: Bad magician!\n", ind++);
            fprintf(out, "Case #%d: Bad magician!\n", ind++);
        if(!cont)
            //printf("Case #%d: Volunteer cheated!\n", ind++);
            fprintf(out, "Case #%d: Volunteer cheated!\n", ind++);
    }

    return 0;
}
