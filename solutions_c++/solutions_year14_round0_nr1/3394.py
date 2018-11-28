#include <stdio.h>

int search(int *ptr, int n)
{
    int i;
    for(i=0; i<4; i++)
    {
        if(n == *(ptr+i))
            return i;
    }
return -1;
}

int main ()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);

    int noofcases, i, row1, row2, temp, count=0, j, k, index;
    int array1[4][4];
    int array2[4];

    scanf("%d",&noofcases);

    for(i=0; i<noofcases; i++)
    {
        scanf("%d",&row1);
        for(j=0; j<4; j++)
        {
            for(k=0; k<4; k++)
            {
                scanf("%d",&array1[j][k]);
            }
        }

        scanf("%d",&row2);

        for(j=0; j<4; j++)
        {
            for(k=0; k<4; k++)
            {
                if(j == row2-1)
                    scanf("%d",&array2[k]);
                else
                    scanf("%d",&temp);

            }
        }

        for(j=0; j<4; j++)
        {
            temp = search(array2, array1[row1-1][j]);

            if(temp!= -1 && count == 0)
                {
                    count++;
                    index = temp;
                }
            else if(temp!=-1 && count != 0)
            {
                count++;
            }

        }
        printf("Case #%d: ",i+1);
        switch(count)
        {
            case 0:
                    printf("Volunteer cheated!\n");
                    break;
            case 1:
                    printf("%d\n",array2[index]);
                    break;
            default:
                    printf("Bad magician!\n");
        }

        count = 0;

    }

return 0;
}
