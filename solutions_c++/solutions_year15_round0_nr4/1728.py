#include <stdio.h>

int table[4][4][4] ={
{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},
{{2,1,2,1},{1,1,1,1},{2,1,2,1},{1,1,1,1}},
{{2,2,2,2},{2,2,1,2},{2,1,1,1},{2,2,1,2}},
{{2,2,2,2},{2,2,2,2},{2,2,2,1},{2,2,1,1}},
};

int main()
{
    int t, x_omino, row, column;

    scanf("%d",&t);
    for(int i = 0 ; i < t ; i++)
    {
        scanf("%d %d %d",&x_omino,&row,&column);
        if(table[x_omino - 1][row - 1][column - 1] == 1)
            printf("Case #%d: GABRIEL\n",i+1);
        else
            printf("Case #%d: RICHARD\n",i+1);
    }

    return 0;
}
