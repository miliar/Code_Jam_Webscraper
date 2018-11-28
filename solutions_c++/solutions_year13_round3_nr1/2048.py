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
    char arr[120];
    int f[120];
    int flag1,flag2,i,j,k,l,fl1,fl2,t,s,n,m,cnt,a,c1,c2;
    long long int sum;
    FILE *fp,*fp2;
    fp=fopen("A-small-attempt0.in","r");
    fp2=fopen("Output10.txt","w");
    if(fp==NULL)
        printf("File not found\n");
    fscanf(fp,"%d",&t);
    for(s=1; s<=t; s++)
    {
    cnt=0;
    fscanf(fp,"%s",arr);
    fscanf(fp,"%d",&n);
    for(i=0;i<strlen(arr);i++)
     {
         switch(arr[i])
             {
            case 'a': case 'e': case 'i': case 'o': case 'u':
                {
                    f[i]=0;
                    break;
                }
                default: f[i]=1;
             }
     }
     for(i=0;i<strlen(arr);i++)
     {
        for(j=i+n-1;j<strlen(arr);j++)
        {
            fl2=0;
            for(k=i;k<=j-n+1;k++)
            {
                fl1=0;
                for(l=k;l<=k+n-1;l++)
                {
                    if(f[l]==1)
                        fl1++;
                }
                if(fl1==n)
                {
                    fl2=1;
                    break;
                }
            }
            if(fl2==1)
                cnt++;
        }
     }
    fprintf(fp2,"Case #%d: ",s);
    fprintf(fp2,"%d\n",cnt);
    }
return 0;
}
