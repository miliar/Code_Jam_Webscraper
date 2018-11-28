#include<stdio.h>
#include<cstring>
int a[102][102];
int greatest_row[102],greatest_col[102];
int main()
{
    int test_cases,n,m;
    bool not_possible;
    scanf("%d",&test_cases);
    for(int i=0;i<test_cases;i++)
    {
        scanf("%d%d",&n,&m);
        not_possible=false;
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                scanf("%d",&a[j][k]);
            }
        }
        memset(greatest_row,0,sizeof(greatest_row));
        memset(greatest_col,0,sizeof(greatest_col));
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                if(greatest_row[j]<a[j][k])
                {
                    greatest_row[j]=a[j][k];
                }
            }
        }
        for(int k=0;k<m;k++)
        {
            for(int j=0;j<n;j++)
            {
                if(greatest_col[k]<a[j][k])
                {
                    greatest_col[k]=a[j][k];
                }
            }
        }
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                if(a[j][k]==greatest_row[j])
                    continue;
                if(a[j][k]==greatest_col[k])
                    continue;
                not_possible=true;
                break;
            }
            if(not_possible)
            {
                break;
            }
        }
        if(not_possible)
        {
            printf("Case #%d: NO\n",i+1);
        }
        else
        {
            printf("Case #%d: YES\n",i+1);
        }
    }
}
