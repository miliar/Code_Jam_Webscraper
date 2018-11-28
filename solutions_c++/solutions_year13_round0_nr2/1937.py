#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    FILE *fp;
    fp=fopen("output3.txt","w");
    int l=0;
    while(t--)
    {

    l++;
    int a[101][101];
    int rmax[101],cmax[101];
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++)
    {

        for(int j=0;j<m;j++)
            scanf("%d",&a[i][j]);
    }
    for(int i=0;i<n;i++)
    {
        rmax[i]=a[i][0];
        for(int j=1;j<m;j++)
        {
            if(a[i][j]>rmax[i])
            {
                rmax[i]=a[i][j];
            }
        }

    }
    for(int j=0;j<m;j++)
    {
        cmax[j]=a[0][j];
        for(int i=1;i<n;i++)
        {
            if(a[i][j]>cmax[j])
            {
                cmax[j]=a[i][j];
            }
        }

    }
    int ans=1;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(a[i][j]<rmax[i])
            {
                if(a[i][j]!=cmax[j])
                {
                    ans=0;
                }
            }

        }

    }
    if(ans==0)
        fprintf(fp,"Case #%d: NO\n",l);
    else
        fprintf(fp,"Case #%d: YES\n",l);
    }
    return 0;
}
