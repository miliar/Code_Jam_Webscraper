#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t, ch, y = 0;
    int a[4][4];
    int p[2];
    int sa[4];
    scanf("%d",&t);
    while(t--)
    {
        y++;
        p[0] = 0;
        p[1] = 0;
        scanf("%d",&ch);
        for(int i = 0; i<4 ; ++i)
        {
            for(int j =0; j<4 ; ++j)
                scanf("%d",&a[i][j]);
        }
        for(int i = 0 ; i<4 ; ++i)
            sa[i] = a[ch-1][i];
        scanf("%d",&ch);
        for(int i = 0; i<4 ; ++i)
        {
                for(int j = 0 ; j<4 ; ++j)
                    scanf("%d",&a[i][j]);
        }
        for(int i = 0 ; i<4 ; ++i)
        {
            for(int j = 0; j<4 ; ++j)
            {
                if(sa[i] == a[ch-1][j])
                {

                    if(p[0]==0)
                        p[0] = sa[i];
                    else
                        p[1] = sa[i];
                }
            }
        }
        if(p[0]!=0&&p[1]!=0)
            printf("Case #%d: Bad magician!\n",y);
        else if( p[0]== 0&&p[1] ==0)
            printf("Case #%d: Volunteer cheated!\n",y);
        else
            printf("Case #%d: %d\n",y,p[0]);
    }
    return 0;
}
