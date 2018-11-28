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
int int_cmp(const void *a, const void *b)
{
    const int *ia = (const int *)a; // casting pointer types
    const int *ib = (const int *)b;
    return *ia - *ib;
}
int main()
{
    int arr[20];
    int flag1,flag2,i,j,k,l,fl1,fl2,t,s,n,m,cnt,a,c1,c2;
    FILE *fp,*fp2;
    fp=fopen("A-small-attempt1.in","r");
    fp2=fopen("Output5.txt","w");
    if(fp==NULL)
        printf("File not found\n");
    fscanf(fp,"%d",&t);
    for(s=1; s<=t; s++)
    {
        cnt=0;
        fscanf(fp,"%d%d",&a,&n);
        for(i=0; i<n; i++)
            fscanf(fp,"%d",&arr[i]);
        qsort(arr,n,sizeof(int),int_cmp);
        //for(i=0;i<n;i++)
            //printf("%d ",arr[i]);
        //printf("\n");
        if(a==1)
            cnt=n;
        else
        {
        for(i=0; i<n; i++)
        {
            if(a>arr[i])
                a=a+arr[i];
            else
            {
                c1=0;
                fl1=a;
                while(fl1<=arr[i])
                {
                    fl1=2*fl1-1;
                    c1++;
                }
                c2=n-i;
                if(c1<c2)
                {
                    a=fl1+arr[i];
                    cnt+=c1;
                }
                else
                {
                    cnt+=c2;
                    break;
                }
            }
        }
        }
    fprintf(fp2,"Case #%d: ",s);
    fprintf(fp2,"%d\n",cnt);
    }
return 0;
}
