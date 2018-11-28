#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;
int main(void)
{
    //freopen("A-small-attempt2.in" , "r" ,stdin);
    //freopen("laobi.out" , "w" , stdout);
    int casenum;
    scanf("%d",&casenum);
    for(int k=1;k<=casenum;k++)
    {
        int qian[5][5],hou[5][5];
        int a,b;
        scanf("%d",&a);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&qian[i][j]);
        int temp[20];
        for(int i=1;i<=16;i++)
            temp[i]=0;
        for(int j=1;j<=4;j++)
            temp[ qian[a][j]  ]=1;
        scanf("%d",&b);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&hou[i][j]);
            int ans=0;
            int res;
         for(int j=1;j<=4;j++)
         {
            if(temp[ hou[b][j]  ]==1)
            {ans++;res=hou[b][j];}
         }
         if(ans==0)
            printf("Case #%d: Volunteer cheated!\n",k);
         else if(ans==1)
            printf("Case #%d: %d\n",k,res);
         else
            printf("Case #%d: Bad magician!\n",k);
    }
    return 0;
}
