//lawnmover

#include<stdio.h>

int A[101][101];
int colmax[101],rowmax[101];

int main()
{
    int t,n,m,l,i,j,max,min,flag;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        scanf("%d",&n);
        scanf("%d",&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&A[i][j]);
            }
        }
        for(i=0;i<n;i++)
        {
            max=0;
            for(j=0;j<m;j++)
            {
                if(A[i][j]>max)
                {
                    max=A[i][j];
                }
            }
            rowmax[i]=max;
        }
        for(j=0;j<m;j++)
        {
            max=0;
            for(i=0;i<n;i++)
            {
                if(A[i][j]>max)
                {
                    max=A[i][j];
                }
            }
            colmax[j]=max;
        }
        flag=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(rowmax[i]>colmax[j])
                {
                    min=colmax[j];
                }
                else
                {
                    min=rowmax[i];
                }
                if(min!=A[i][j])
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
            {
                break;
            }
        }
        if(flag==1)
        {
            printf("Case #%d: NO\n",l);
        }
        else
        {
            printf("Case #%d: YES\n",l);
        }

    }



    return 0;
}
