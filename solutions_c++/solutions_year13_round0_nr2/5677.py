#include<iostream>
#include<cstdio>
 
using namespace std;
 
int row(int i,int s[200][200],int n,int m)
{
    int k=0;
    for(k=0;k<m;k++)
    {
        if(s[i][k]!=1)
        return 0;
    }
    return 1;
}
 
int col(int j,int s[200][200],int n,int m)
{
    int k=0;
    for(k=0;k<n;k++)
    {
        if(s[k][j]!=1)
        return 0;
    }
    return 1;
}
 
int main()
{
    int t,k,i,j,n,m;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        int s[200][200],check1=1,check2=1,visirowt[200]={0},visicolt[200]={0},flag=0;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&s[i][j]);
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(s[i][j]==1)
                {
                    check1=row(i,s,n,m);
                    check2=col(j,s,n,m);
                if(check1==1 || check2==1)
                {
                    continue;
                }
                else
                {
                    flag=1;
                    goto abc;
                }
                }
            }
        }
        abc:
        if(!flag)
        {
            printf("Case #%d: YES\n",k);
        }
        else
        {
            printf("Case #%d: NO\n",k);
        }
    }
    return 0;
}