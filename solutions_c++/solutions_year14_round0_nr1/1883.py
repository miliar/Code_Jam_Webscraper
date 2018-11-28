#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
//    freopen("A-s.in","r",stdin);
//    freopen("out.txt","w",stdout);
    int one[15][15],two[15][15],t,n,m;
    scanf("%d",&t);
    for(int cs=1; cs<=t; cs++)
    {
        scanf("%d",&n);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
                scanf("%d",&one[i][j]);
        }
        scanf("%d",&m);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
                scanf("%d",&two[i][j]);
        }
        int ct=0,ans=0;
        n--;
        m--;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
//                printf("%d %d\n",one[n][i],two[m][j]);
                if(one[n][i]==two[m][j])
                {
                    ct++;
                    ans=one[n][i];
                }
            }
        }
        if(ct==1)
            printf("Case #%d: %d\n",cs,ans);
        else if(ct==0)
            printf("Case #%d: Volunteer cheated!\n",cs);
        else
            printf("Case #%d: Bad magician!\n",cs);

    }
return 0;
}
