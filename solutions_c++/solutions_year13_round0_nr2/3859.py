#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<limits.h>

int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}
int main()
{
    int arr[110][110];
    int flag1,flag2,i,j,k,l,fl1,fl2,t,s,n,m,cnt;
    FILE *fp,*fp2;
    fp=fopen("B-large.in","r");
    fp2=fopen("Output1.txt","w");
    if(fp==NULL)
        printf("File not found\n");
    fscanf(fp,"%d",&t);
    for(s=1; s<=t; s++)
    {
        fscanf(fp,"%d%d",&n,&m);
        for(i=1; i<=n; i++)
        {
            for(j=1; j<=m; j++)
            {
                fscanf(fp,"%d",&arr[i][j]);
            }
        }
        cnt=0;
        for(i=1; i<=n; i++)
        {
            for(j=1; j<=m; j++)
            {
                l=arr[i][j];
                fl1=0;
                fl2=0;
                for(k=1; k<=m; k++)
                {
                    if(arr[i][k]>l)
                    {
                        fl1=1;
                        break;
                    }
                }
                for(k=1; k<=n; k++)
                {
                    if(arr[k][j]>l)
                    {
                        fl2=1;
                        break;
                    }
                }
                if(fl1==0 || fl2==0)
                    cnt++;
            }
        }
        fprintf(fp2,"Case #%d: ",s);
        if(cnt==(n*m))
            fprintf(fp2,"YES\n");
        else fprintf(fp2,"NO\n");
    }
        return 0;
}
