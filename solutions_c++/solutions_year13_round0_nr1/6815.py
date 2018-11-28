#include<cstdio>

char tab[4][4];

bool czyx(int a)
{
    if(tab[a/4][a%4]=='X' || tab[a/4][a%4]=='T')
        return true;
    return false;
}

bool czyo(int a)
{
    if(tab[a/4][a%4]=='O' || tab[a/4][a%4]=='T')
        return true;
    return false;
}

bool czyk(int a)
{
    if(tab[a/4][a%4]=='.')
        return true;
    return false;
}

int sprawdz()
{
    if(czyx(0) && czyx(1) && czyx(2) && czyx(3))
        return 1;
    if(czyx(4) && czyx(5) && czyx(6) && czyx(7))
        return 1;
    if(czyx(8) && czyx(9) && czyx(10) && czyx(11))
        return 1;
    if(czyx(12) && czyx(13) && czyx(14) && czyx(15))
        return 1;
    if(czyx(0) && czyx(4) && czyx(8) && czyx(12))
        return 1;
    if(czyx(1) && czyx(5) && czyx(9) && czyx(13))
        return 1;
    if(czyx(2) && czyx(6) && czyx(10) && czyx(14))
        return 1;
    if(czyx(3) && czyx(7) && czyx(11) && czyx(15))
        return 1;
    if(czyx(0) && czyx(5) && czyx(10) && czyx(15))
        return 1;
    if(czyx(3) && czyx(6) && czyx(9) && czyx(12))
        return 1;
    if(czyo(0) && czyo(1) && czyo(2) && czyo(3))
        return 2;
    if(czyo(4) && czyo(5) && czyo(6) && czyo(7))
        return 2;
    if(czyo(8) && czyo(9) && czyo(10) && czyo(11))
        return 2;
    if(czyo(12) && czyo(13) && czyo(14) && czyo(15))
        return 2;
    if(czyo(0) && czyo(4) && czyo(8) && czyo(12))
        return 2;
    if(czyo(1) && czyo(5) && czyo(9) && czyo(13))
        return 2;
    if(czyo(2) && czyo(6) && czyo(10) && czyo(14))
        return 2;
    if(czyo(3) && czyo(7) && czyo(11) && czyo(15))
        return 2;
    if(czyo(0) && czyo(5) && czyo(10) && czyo(15))
        return 2;
    if(czyo(3) && czyo(6) && czyo(9) && czyo(12))
        return 2;
    for(int i=0; i<16; i++)
        if(czyk(i))
            return 3;
    return 4;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
        for(int j=0; j<4; j++)
            scanf("%s", tab[j]);
        printf("Case #%d: ", i);
        int d = sprawdz();
        if(d==1)
            printf("X won\n");
        else if(d==2)
            printf("O won\n");
        else if(d==3)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
}
