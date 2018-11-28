#include <stdio.h>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int N;
    scanf("%d",&N);
    for(int I=1;I<=N;I++)
    {
        int n,aux;
        int res[20]={0};
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                {
                    scanf("%d",&aux);
                    if(i==n)
                        res[aux]++;
                }
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                {
                    scanf("%d",&aux);
                    if(i==n)
                        res[aux]++;
                }
        int cont=0;
        for(int i=1;i<=16;i++)
            if(res[i]==2)
                cont++;
        if(I>1)
            printf("\n");
        printf("Case #%d: ",I);
        if(cont==0)
        {
            printf("Volunteer cheated!");
            continue;
        }
        if(cont>1)
        {
            printf("Bad magician!");
            continue;
        }
        for(int i=1;i<=16;i++)
        {
            if(res[i]==2)
                printf("%d",i);
        }
    }
    return 0;
}
