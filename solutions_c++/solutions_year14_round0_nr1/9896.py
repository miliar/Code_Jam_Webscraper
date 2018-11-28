#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int t,a,b,m1[6][6],m2[6][6],i,j,ct,ans,k;
    scanf("%d",&t);
    while(t--)
    {
        k++;
        scanf("%d",&a);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&m1[i][j]);

        scanf("%d",&b);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&m2[i][j]);
        ct=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                if(m1[a][i]==m2[b][j])
                    {
                        ct++;
                        ans=m1[a][i];
                    }
            }
        if(ct==1)
        {
            printf("Case #%d: %d\n",k,ans);
        }
        else if(ct>1)
        {
            printf("Case #%d: Bad magician!\n",k);
        }
        else if(ct==0)
            printf("Case #%d: Volunteer cheated!\n",k);
    }
    return 0;
}
