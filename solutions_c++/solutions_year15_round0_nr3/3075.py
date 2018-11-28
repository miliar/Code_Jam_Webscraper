//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
const int LX = 10004;
char R[256][256];

void Init()
{
    R['1']['1'] = '1';
    R['1']['i'] = 'i';
    R['1']['j'] = 'j';
    R['1']['k'] = 'k';
    R['i']['1'] = 'i';
    R['i']['i'] = -'1';
    R['i']['j'] = 'k';
    R['i']['k'] = -'j';
    R['j']['1'] = 'j';
    R['j']['i'] = -'k';
    R['j']['j'] = -'1';
    R['j']['k'] = 'i';
    R['k']['1'] = 'k';
    R['k']['i'] = 'j';
    R['k']['j'] = -'i';
    R['k']['k'] = -'1';
}
char mnoz(char a, char b)
{
    char wyn = 1;
    if(a < 0)
    {
        wyn *= -1;
        a *= -1;
    }
    if(b < 0)
    {
        wyn *= -1;
        b *= -1;
    }
    
    return wyn*R[a][b];
}

int L, X;
char tab[LX];

int szukaj(int start, char co)
{
    char ter = '1';
    for(int i = start;i <= L*X;i++)
    {
        ter = mnoz(ter, tab[i]);
        if(ter == co)
            return i;
    }
    return L*X+1;
}

char obl(int a, int b)
{
    char ter = '1';
    for(int i = a;i <= b;i++)
        ter = mnoz(ter, tab[i]);
    return ter;
}

int main()
{
    Init();
    
    int t;
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d", &L, &X);
        for(int i = 1;i <= L;i++)
            scanf(" %c", &tab[i]);
        for(int i = 2;i <= X;i++)
            for(int j = 1;j <= L;j++)
                tab[(i-1)*L+j] = tab[j];
            
        int a = szukaj(1, 'i');
        int b = szukaj(a+1, 'j');
        int c = szukaj(b+1, 'k');
        char ost = obl(c+1, L*X);
        
        bool wyn;
        if(c <= L*X && ost == '1') wyn = true;
        else wyn = false;
        
        printf("Case #%d: %s\n", ti, (wyn ? "YES" : "NO"));
    }
    return 0;
}
