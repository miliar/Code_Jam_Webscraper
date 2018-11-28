#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    int r1,r2;
    int shu1[5][5],shu2[5][5];
    int t;
    int i,j;
    int tmp;
    int ans;
    int da;
    scanf("%d",&cases);
    for(t=1;t<=cases;++t)
    {
        printf("Case #%d: ",t);
        scanf("%d",&r1);
        for(i=1;i<5;++i)
            for(j=1;j<5;++j)
                scanf("%d",&shu1[i][j]);
        scanf("%d",&r2);
        for(i=1;i<5;++i)
            for(j=1;j<5;++j)
                scanf("%d",&shu2[i][j]);
        ans=0;
        for(i=1;i<5;++i)
        {
            tmp=0;
            for(j=1;j<5;++j)
            {
                if(shu1[r1][i]==shu2[r2][j])
                    tmp=shu1[r1][i];
            }
            if(tmp)
            {
                ans++;
                da=tmp;
            }
        }
        if(ans==0)
            printf("Volunteer cheated!");
        if(ans==1)
            printf("%d",da);
        if(ans>1)
            printf("Bad magician!");
        printf("\n");
    }
    return 0;
}
