#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,k,i,j,a;
    int color[20];
    scanf("%d",&t);
    for(k=1; k<=t; k++)
    {
        int ans1,ans2;
        for(i=1; i<=16; i++)
            color[i]=0;
        scanf("%d",&ans1);
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                scanf("%d",&a);
                if(i==ans1)
                    color[a]=1;
            }
        }
        scanf("%d",&ans2);
        int sum=0,num;
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                scanf("%d",&a);
                if(i==ans2&&color[a])
                {
                    sum++;
                    num=a;
                }
            }
        }
        printf("Case #%d: ",k);
        if(sum>1)
            printf("Bad magician!\n");
        else if(sum==0)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n",num);
    }
    return 0;
}
