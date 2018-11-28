#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;
int map[105][105];
int n,m;
int solve()
{
    int i,j,k;
    int f1,f2;
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
    {
        f1=f2=0;
        int tmp=map[i][j];
        for(k=i-1;k>=0;k--)
            if(tmp<map[k][j])
        {
            f1++;
            break;
        }
        for(k=i+1;k<n;k++)
            if(tmp<map[k][j])
        {
            f1++;
            break;
        }
        for(k=j-1;k>=0;k--)
            if(tmp<map[i][k])
        {
            f2++;
            break;
        }
        for(k=j+1;k<m;k++)
            if(tmp<map[i][k])
        {
            f2++;
            break;
        }
        if(f1&&f2)
            return 0;
    }
    return 1;
}
int main()
{
    FILE *fp1,*fp2;
    fp1=fopen("B-large.in","r");
    fp2=fopen("B-large.out","w");
    int i,j,k;
    int t,ca;
    fscanf(fp1,"%d",&ca);
    printf("%d\n",ca);
    for(t=1;t<=ca;t++)
    {
        fscanf(fp1,"%d%d",&n,&m);
        printf("%d %d\n",n,m);
        for(i=0;i<n;i++)
            for(j=0;j<m;j++)
            fscanf(fp1,"%d",&map[i][j]);
        for(i=0;i<n;i++)
        {
             for(j=0;j<m;j++)
            printf("%d ",map[i][j]);
            printf("\n");
        }

            fprintf(fp2,"Case #%d: ",t);
            printf("Case #%d: ",t);
        if(solve())
        {
              fprintf(fp2,"YES\n");
              printf("YES\n");
        }

        else
        {
             fprintf(fp2,"NO\n");
             printf("NO\n");
        }
        // system("pause");
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
