#include <cstdio>
#include <cstring>
#include <map>
#include <iostream>

using namespace std;
int checkwin(char map[20])
{
    if((map[1]=='X' || map[1]=='T') && (((map[1]==map[6] || map[6]=='T' || map[6]=='X') && (map[6]==map[11] || map[11]=='T' || map[11]=='X') && (map[11]==map[16] || map[16]=='T' || map[16]=='X')) || ((map[1]==map[5] || map[5]=='T' || map[5]=='X') && (map[5]==map[9] || map[9]=='T' || map[9]=='X') && (map[9]==map[13] || map[13]=='T' || map[13]=='X')) || ((map[1]==map[2] || map[2]=='T' || map[2]=='X') && (map[2]==map[3] || map[3]=='T' || map[3]=='X') && (map[3]==map[4] || map[4]=='T' || map[4]=='X'))))
        return 1;
    else if((map[1]=='O' || map[1]=='T') && (((map[1]==map[6] || map[6]=='T' || map[6]=='O') && (map[6]==map[11] || map[11]=='T' || map[11]=='O') && (map[11]==map[16] || map[16]=='T' || map[16]=='O')) || ((map[1]==map[5] || map[5]=='T' || map[5]=='O') && (map[5]==map[9] || map[9]=='T' || map[9]=='O') && (map[9]==map[13] || map[13]=='T' || map[13]=='O')) || ((map[1]==map[2] || map[2]=='T' || map[2]=='O') && (map[2]==map[3] || map[3]=='T' || map[3]=='O') && (map[3]==map[4] || map[4]=='T' || map[4]=='O'))))
        return 2;
    else if((map[5]=='X' || map[5]=='T') && ((map[5]==map[6] || map[6]=='T' || map[6]=='X') && (map[6]==map[7] || map[7]=='T' || map[7]=='X') && (map[7]==map[8] || map[8]=='T' || map[8]=='X')))
        return 1;
    else if((map[5]=='O' || map[5]=='T') && ((map[5]==map[6] || map[6]=='T' || map[6]=='O') && (map[6]==map[7] || map[7]=='T' || map[7]=='O') && (map[7]==map[8] || map[8]=='T' || map[8]=='O')))
        return 2;
    else if((map[9]=='X' || map[9]=='T') && ((map[9]==map[10] || map[10]=='T' || map[10]=='X') && (map[10]==map[11] || map[11]=='T' || map[11]=='X') && (map[11]==map[12] || map[12]=='T' || map[12]=='X')))
        return 1;
    else if((map[9]=='O' || map[9]=='T') && ((map[9]==map[10] || map[10]=='T' || map[10]=='O') && (map[10]==map[11] || map[11]=='T' || map[11]=='O') && (map[11]==map[12] || map[12]=='T' || map[12]=='O')))
        return 2;
    else if((map[13]=='X' || map[13]=='T') && ((map[13]==map[14] || map[14]=='T' || map[14]=='X') && (map[14]==map[15] || map[15]=='T' || map[15]=='X') && (map[15]==map[16] || map[16]=='T' || map[16]=='X')))
        return 1;
    else if((map[13]=='O' || map[13]=='T') && ((map[13]==map[14] || map[14]=='T' || map[14]=='O') && (map[14]==map[15] || map[15]=='T' || map[15]=='O') && (map[15]==map[16] || map[16]=='T' || map[16]=='O')))
        return 2;
    else if((map[2]=='X' || map[2]=='T') && ((map[2]==map[6] || map[6]=='T' || map[6]=='X') && (map[6]==map[10] || map[10]=='T' || map[10]=='X') && (map[10]==map[14] || map[14]=='T' || map[14]=='X')))
        return 1;
    else if((map[2]=='O' || map[2]=='T') && ((map[2]==map[6] || map[6]=='T' || map[6]=='O') && (map[6]==map[10] || map[10]=='T' || map[10]=='O') && (map[10]==map[14] || map[14]=='T' || map[14]=='O')))
        return 2;
    else if((map[3]=='X' || map[3]=='T') && ((map[3]==map[7] || map[7]=='T' || map[7]=='X') && (map[7]==map[11] || map[11]=='T' || map[11]=='X') && (map[11]==map[15] || map[15]=='T' || map[15]=='X')))
        return 1;
    else if((map[3]=='O' || map[3]=='T') && ((map[3]==map[7] || map[7]=='T' || map[7]=='O') && (map[7]==map[11] || map[11]=='T' || map[11]=='O') && (map[11]==map[15] || map[15]=='T' || map[15]=='O')))
        return 2;
    else if((map[4]=='X' || map[4]=='T') && (((map[4]==map[8] || map[8]=='T' || map[8]=='X') && (map[8]==map[12] || map[12]=='T' || map[12]=='X') && (map[12]==map[16] || map[16]=='T' || map[16]=='X')) || ((map[4]==map[7] || map[7]=='T' || map[7]=='X') && (map[7]==map[10] || map[10]=='T' || map[10]=='X') && (map[10]==map[13] || map[13]=='T' || map[13]=='X'))))
        return 1;
    else if((map[4]=='O' || map[4]=='T') && (((map[4]==map[8] || map[8]=='T' || map[8]=='O') && (map[8]==map[12] || map[12]=='T' || map[12]=='O') && (map[12]==map[16] || map[16]=='T' || map[16]=='O')) || ((map[4]==map[7] || map[7]=='T' || map[7]=='O') && (map[7]==map[10] || map[10]=='T' || map[10]=='O') && (map[10]==map[13] || map[13]=='T' || map[13]=='O'))))
        return 2;
    else if(map[1]=='.' || map[2]=='.' || map[3]=='.' || map[4]=='.' || map[5]=='.' || map[6]=='.' || map[7]=='.' || map[8]=='.' || map[9]=='.' || map[10]=='.' || map[11]=='.' || map[12]=='.' || map[13]=='.' || map[14]=='.' || map[15]=='.' || map[16]=='.')
        return 0;
    else
        return -1;
}

int main()
{
    int t;
    char field[10][10];
    char map[20];
    freopen("A-large.in", "r", stdin);
    freopen("tictactoe.o", "w", stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int index=0;
        for(int j=0;j<=3;j++)
        {
            scanf("%s",&field[index]);
            index++;
        }
        index=1;
        for(int j=0;j<=3;j++)
        {
            for(int k=0;k<=3;k++)
            {
                map[index]=field[j][k];
                index++;
            }
        }
        if(checkwin(map)==-1)
            printf("Case #%d: Draw\n",i);
        else if(checkwin(map)==0)
            printf("Case #%d: Game has not completed\n",i);
        else if(checkwin(map)==1)
            printf("Case #%d: X won\n",i);
        else if(checkwin(map)==2)
            printf("Case #%d: O won\n",i);
    }
}
