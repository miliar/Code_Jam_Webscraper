#include <iostream>
#include <cstdio>

using namespace std;

int used[20];
int mat[5][5];
int t, r;

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%i", &t);
    for(int ti=0; ti<t; ti++)
    {
        scanf("%i", &r);
        r--;
        for(int i=0; i<16; i++)
            scanf("%i", &mat[i/4][i%4]);
        for(int i=0; i<4; i++)
            used[mat[r][i]]++;
        scanf("%i", &r);
        r--;
        for(int i=0; i<16; i++)
            scanf("%i", &mat[i/4][i%4]);
        for(int i=0; i<4; i++)
            used[mat[r][i]]++;
        bool badm=false;
        bool cheat=true;
        int rez;
        for(int i=0; i<16; i++)
        {
            if(used[i+1]==2)
            {
                if(!cheat) badm=true;
                cheat=false;
                rez=i+1;
            }
        }
        for(int i=0; i<16; i++)
        {
            //printf("%i %i\n", i+1, used[i+1]);
            used[i+1]=0;
        }
        if(badm) printf("Case #%i: Bad magician!\n", ti+1);
        else if(cheat) printf("Case #%i: Volunteer cheated!\n", ti+1);
        else printf("Case #%i: %i\n", ti+1, rez);
    }
    return 0;
}
/*
100
1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
4
1 5 9 13
2 6 10 14
3 7 11 15
4 8 12 16
*/
