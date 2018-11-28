#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#define pi 2*acos(0)
#define inf INT_MAX
#define eps 0.00000001
using namespace std;

main()
{
    int i,j,k,row,col,flag,flag1,flag2,arr[110][110],p,t;
    FILE *read,*write;
    read=fopen("codejam3largein.txt","r");
    write=fopen("codejam3largeout.txt","w");
    fscanf(read," %d",&t);
    for(p=1;p<=t;p++)
    {
        fscanf(read," %d %d",&row,&col);
        for(i=1;i<=row;i++)
        {
            for(j=1;j<=col;j++)
            {
                fscanf(read," %d",&arr[i][j]);
            }
        }
        flag=0;
        for(i=1;i<=row&&flag==0;i++)
        {
            for(j=1;j<=col&&flag==0;j++)
            {
                    flag1=0;
                    flag2=0;
                    for(k=j-1;k>=1;k--)
                    {if(arr[i][k]>arr[i][j])
                    {flag1=1;
                    break;}}
                    for(k=j+1;k<=col;k++)
                    {if(arr[i][k]>arr[i][j])
                    {flag1=1;
                    break;}}
                    for(k=i-1;k>=1;k--)
                    {if(arr[k][j]>arr[i][j])
                    {flag2=1;
                    break;}}
                    for(k=i+1;k<=row;k++)
                    {if(arr[k][j]>arr[i][j])
                    {flag2=1;
                    break;}}
                    if(flag1==1&&flag2==1)
                    flag=1;
            }
        }
        if(flag==0)
        fprintf(write,"Case #%d: YES\n",p);
        else
        fprintf(write,"Case #%d: NO\n",p);
    }
    fclose(read);
    fclose(write);
    return 0;
}

