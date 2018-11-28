#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

bool res1[17];
int temp[20];
int main()
{
    int t;
    int a,b;
    //freopen("e:\\b.txt","r",stdin);
    //freopen("e:\\f.txt","w",stdout);
    scanf("%d",&t);
    int count=0;
    while(t--)
    {
        memset(res1,0,sizeof(res1));
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
        {
            int x1,x2,x3,x4;

            scanf("%d %d %d %d",&x1,&x2,&x3,&x4);
            if(i==a)
            {
                res1[x1]=1;
                res1[x2]=1;
                res1[x3]=1;
                res1[x4]=1;
            }
        }
        scanf("%d",&b);
        int ans=0;
        for(int i=1;i<=4;i++)
        {
            int x1,x2,x3,x4;
            scanf("%d %d %d %d",&x1,&x2,&x3,&x4);
            if(i==b)
            {
                if(res1[x1])
                {
                    temp[ans++]=x1;
                }
                if(res1[x2])
                {
                    temp[ans++]=x2;
                }
                if(res1[x3])
                {
                    temp[ans++]=x3;
                }
                if(res1[x4])
                {
                    temp[ans++]=x4;
                }
            }
        }
        printf("Case #%d: ",++count);
        if(ans==1)
        {
            printf("%d\n",temp[0]);
        }
        else if(ans<1)
        {
            printf("Volunteer cheated!\n");
        }
        else
        {
            printf("Bad magician!\n");
        }
    }
    return 0;
}
