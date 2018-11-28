#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int arr1[4][4]={0},arr2[4][4]={0},x,y,flag=0,num=0;
        scanf("%d",&x);
        for(int j=0;j<4;j++)
        for(int k=0;k<4;k++)
        scanf("%d",&arr1[j][k]);
        scanf("%d",&y);
        for(int j=0;j<4;j++)
        for(int k=0;k<4;k++)
        scanf("%d",&arr2[j][k]);

        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
        {
            if(arr1[x-1][j]==arr2[y-1][k])
              {
                  ++flag;
                if(flag==1)
                    num=arr1[x-1][j];
                    if(flag==2)
                        break;
              }
                  if(flag==2)
                        break;
        }
        if (flag==0)
            printf("Case #%d: Volunteer cheated!\n",i);
            else if(flag>1)
                printf("Case #%d: Bad magician!\n",i);
            else
                printf("Case #%d: %d\n",i,num);
    }
}
