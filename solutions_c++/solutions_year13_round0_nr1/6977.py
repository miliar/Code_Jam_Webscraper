#include<cstdio>
#include<iostream>
using namespace std;

int check(int mat[][4])
{
    int win[10][4] = { {0,1,2,3},   {4,5,6,7},  {8,9,10,11}, {12,13,14,15},
                       {0,4,8,12},  {1,5,9,13}, {2,6,10,14}, {3,7,11,15},
                       {0,5,10,15}, {3,6,9,12}
                    };
    int bf = 0;
    for(int x=0;x<10;x++)
    {
        int s=0,i,j;
        for(int y=0;y<4;y++)
        {
            i=win[x][y]/4;j=win[x][y]%4;
            s+=mat[i][j];
            if(mat[i][j]==0)  bf = 1;
        }
        if(s==4 || s==13)
            return 1;
        if(s==-4 || s==7)
            return 2;
    }
    if(bf)
        return 4;
    return 3;
}

int main()
{
    int c;
    scanf("%d",&c);
    int a[4][4];
    for(int x=0;x<c;x++)
    {
        char s,t;
        scanf("%c",&t);
        for(int y=0;y<4;y++)
        { for(int z=0;z<4;z++)
            {
                scanf("%c",&s);
                if(s=='X')
                    a[y][z] = 1;
                else if(s=='O')
                    a[y][z] = -1;
                else if(s=='.')
                    a[y][z] = 0;
                else
                    a[y][z] = 10;

            }
            scanf("%c",&t);
        }
        int r = check(a);
        printf("Case #%d: ",x+1);
        switch(r)
        {
            case 1: printf("X won\n");break;
            case 2: printf("O won\n");break;
            case 3: printf("Draw\n");break;
            case 4: printf("Game has not completed\n");break;
        }
    }
    return 0;
}
