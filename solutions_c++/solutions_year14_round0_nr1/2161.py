#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int a[5],b[5];
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ncase;
    int T=0;
    int i,j;
    scanf("%d",&ncase);
    while(ncase--)
    {
        int x,y;
        scanf("%d",&x);
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&y);
                if(i==x)
                    a[j]=y;
            }
        }
        scanf("%d",&x);
        for(i=1;i<=4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&y);
                if(i==x)
                    b[j]=y;
            }
        }
        int num=0;
        int ans;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i]==b[j])
                {
                    num++;
                    ans=a[i];
                }
            }
        }
        printf("Case #%d: ",++T);
        if(num==1)
            printf("%d\n",ans);
        else if(num==0)
            printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
