#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
int a[5][5],b[5][5];
int main()
{
    int T;
    scanf("%d",&T);
    for(int CounterT=1;CounterT<=T;CounterT++)
    {
        int n;
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        int m;
        scanf("%d",&m);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        printf("Case #%d: ",CounterT);
        int counter=0,ans[10];
        bool sign[17]={false};
        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                if(a[n][j]==b[m][k]&&sign[a[n][j]]==false)
                {
                    sign[a[n][j]]=true;
                    ans[counter++]=a[n][j];
                }
            }
        }
        if(counter==1)
        {
            printf("%d\n",ans[0]);
        }
        else if(counter>1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
