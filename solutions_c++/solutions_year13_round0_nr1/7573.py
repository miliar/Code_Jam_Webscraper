#include <cstdio>

#define WO  1
#define WX  2
#define DR  3
#define NC  4

char tabla[4][5];

int valida()
{
    for(int idx=0;idx<4;idx++)
    {
        if( (tabla[idx][0] == 'O' || tabla[idx][0] == 'T')
         && (tabla[idx][1] == 'O' || tabla[idx][1] == 'T')
         && (tabla[idx][2] == 'O' || tabla[idx][2] == 'T')
         && (tabla[idx][3] == 'O' || tabla[idx][3] == 'T') )
            return WO;

        if( (tabla[idx][0] == 'X' || tabla[idx][0] == 'T')
         && (tabla[idx][1] == 'X' || tabla[idx][1] == 'T')
         && (tabla[idx][2] == 'X' || tabla[idx][2] == 'T')
         && (tabla[idx][3] == 'X' || tabla[idx][3] == 'T') )
            return WX;

        if( (tabla[0][idx] == 'O' || tabla[0][idx] == 'T')
         && (tabla[1][idx] == 'O' || tabla[1][idx] == 'T')
         && (tabla[2][idx] == 'O' || tabla[2][idx] == 'T')
         && (tabla[3][idx] == 'O' || tabla[3][idx] == 'T') )
            return WO;

        if( (tabla[0][idx] == 'X' || tabla[0][idx] == 'T')
         && (tabla[1][idx] == 'X' || tabla[1][idx] == 'T')
         && (tabla[2][idx] == 'X' || tabla[2][idx] == 'T')
         && (tabla[3][idx] == 'X' || tabla[3][idx] == 'T') )
            return WX;
    }

    if( (tabla[0][0] == 'O' || tabla[0][0] == 'T')
     && (tabla[1][1] == 'O' || tabla[1][1] == 'T')
     && (tabla[2][2] == 'O' || tabla[2][2] == 'T')
     && (tabla[3][3] == 'O' || tabla[3][3] == 'T') )
        return WO;

    if( (tabla[0][0] == 'X' || tabla[0][0] == 'T')
     && (tabla[1][1] == 'X' || tabla[1][1] == 'T')
     && (tabla[2][2] == 'X' || tabla[2][2] == 'T')
     && (tabla[3][3] == 'X' || tabla[3][3] == 'T') )
        return WX;

    if( (tabla[0][3] == 'O' || tabla[0][3] == 'T')
     && (tabla[1][2] == 'O' || tabla[1][2] == 'T')
     && (tabla[2][1] == 'O' || tabla[2][1] == 'T')
     && (tabla[3][0] == 'O' || tabla[3][0] == 'T') )
        return WO;

    if( (tabla[0][3] == 'X' || tabla[0][3] == 'T')
     && (tabla[1][2] == 'X' || tabla[1][2] == 'T')
     && (tabla[2][1] == 'X' || tabla[2][1] == 'T')
     && (tabla[3][0] == 'X' || tabla[3][0] == 'T') )
        return WX;

    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if( tabla[i][j] == '.' )
                return NC;

    return DR;
}

main(){

int T, t, i, op;

scanf("%d\n", &T);
for(t=1;t<=T;t++)
{
    op = 0;
    for(i=0;i<4;i++)
        scanf("%s\n", &tabla[i]);

    switch(valida())
    {
        case WO:
            printf("Case #%d: O won\n", t);
            break;

        case WX:
            printf("Case #%d: X won\n", t);
            break;

        case DR:
            printf("Case #%d: Draw\n", t);
            break;

        case NC:
            printf("Case #%d: Game has not completed\n", t);
            break;
    }
}

return 0;
}
