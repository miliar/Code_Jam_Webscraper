#include<stdio.h>
int main()
{
    int a[101][101],i,j,flag,max,t,n,m,min[101],k,l,flag1;
     FILE *fp1,*fp2;
    fp1=fopen("B-small-attempt1.in","r");
    fp2=fopen("Goutput.txt","w");
    fscanf(fp1,"%d",&t);
    l=1;
    while(t--)
    {
        fscanf(fp1,"%d%d",&n,&m);
    
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                fscanf(fp1,"%d",&a[i][j]);
                   
            }
        }
        for(i=0;i<n;i++)
        {
            min[i]=1000;
            for(j=0;j<m;j++)
            {
                if(a[i][j]<min[i])
                min[i]=a[i][j];
            }
        }
        flag=flag1=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]==min[i])
                {
                    for(k=0;k<m;k++)
                    {
                        if(a[i][k]!=min[i])
                        flag=1;
                    }
                    for(k=0;k<n;k++)
                    {
                        if(a[k][j]!=min[i])
                        flag1=1;
                    }
                    if(flag==1 && flag1==1)
                    {
                        break;
                    }
                    else
                    flag=flag1=0;
                }
            }
            if(flag==1 && flag1==1)
            break;
        }
        if(flag==1 && flag1==1)
        fprintf(fp2,"Case #%d: NO\n",l);
        else if(flag==0 && flag1==0)
        fprintf(fp2,"Case #%d: YES\n",l);
        l++;
    }
    return 0;
}
