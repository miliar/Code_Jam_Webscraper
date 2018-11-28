#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,ans1,ans2,a[4][4],b[4][4],temp,counter,ans,num=1;
    scanf("%d",&t);
    while(t--)
    {   counter=0;
        scanf("%d",&ans1);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);
        scanf("%d",&ans2);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            scanf("%d",&b[i][j]);
        for(int i=0;i<4;i++)
        {   temp=a[ans1-1][i];
            for(int j=0;j<4;j++)
            {
                if(temp==b[ans2-1][j])
                {
                    counter++;
                    ans=b[ans2-1][j];
                }
                if(counter==2)
                    break;
            }

        }
        if(counter==1)
            printf("Case #%d: %d\n",num,ans);
        else if(counter==0)
            printf("Case #%d: Volunteer cheated!\n",num);
        else
            printf("Case #%d: Bad magician!\n",num);

        num++;
    }
}
