#include<cstdio>
int odw[20];
void czysc()
{
    for(int a = 0; a < 20; a++)
    {
        odw[a] = 0;
    }
}
int main()
{
    int przyp;
    scanf("%d", &przyp);
    for(int a = 1; a <= przyp; a++)
    {
        czysc();
        int odp,tmp;
        scanf("%d", &odp);
        for(int x = 1; x <= 4; x++)
        {
            for(int y = 1; y <= 4; y++)
            {
                scanf("%d", &tmp);
                if(x == odp)
                {
                    odw[tmp] = 1;
                }
            }
        }
        scanf("%d", &odp);
        int wyn,ile;
        ile = 0;
        for(int x = 1; x <= 4; x++)
        {
            for(int y = 1; y <= 4; y++)
            {
                scanf("%d", &tmp);
                if(x == odp && odw[tmp] == 1)
                {
                    ile++;
                    wyn = tmp;
                }
            }
        }
        if(ile == 0)
        {
            printf("Case #%d: Volunteer cheated!\n", a);
        }
        if(ile == 1)
        {
            printf("Case #%d: %d\n", a, wyn); 
        }
        if(ile > 1)
        {
            printf("Case #%d: Bad magician!\n", a);
        }

    }
    return 0;
}
