#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char str[1005];
long long a,b;
int palin()
{
    int N=strlen(str);
    int i,j;
    for(i=0,j=N-1;;i++,j--)
    {
        if(i>j) break;
        if(str[i]!=str[j]) return 0;
    }
    return 1;
}
int pow2palin()
{
    long long num;
    int N=strlen(str);
    sscanf(str,"%I64d",&num);
    num=num*num;
    if(num>b || num<a) return 0;
    else
    {
        sprintf(str,"%d",num);
        if(palin()) return 1;
        else return 0;
    }
}
main()
{
    freopen("C-small-attempt0.in","r",stdin);
	freopen("outX.txt","w",stdout);

    int n;
    scanf("%d",&n);
    int i,j,k;
    int countt;
    for(i=0;i<n;i++)
    {
        scanf("%I64d %I64d",&a,&b);
        countt=0;
        for(j=1;j<=9;j++)
        {
            sprintf(str,"%d",j*j);
            if(j*j>=a && j*j<=b)
            {
                if(palin()) countt++;
            }
        }
        for(j=1;j<=9;j++)
        {
            sprintf(str,"%d",j);
            str[1]=j-1+'1';
            str[2]='\0';
            if(pow2palin()) countt++;

            sprintf(str,"%d",j);
            str[2]=j-1+'1';
            str[3]='\0';
            for(k=0;k<=9;k++)
            {
                str[1]=k-0+'0';
                if(pow2palin()) countt++;
            }
        }
        for(j=10;j<=99;j++)
        {
            sprintf(str,"%d",j);
            str[2]=str[1];
            str[3]=str[0];
            str[4]='\0';
            if(pow2palin()) countt++;

            sprintf(str,"%d",j);
            str[3]=str[1];
            str[4]=str[0];
            str[5]='\0';
            for(k=0;k<=9;k++)
            {
                str[2]=k-0+'0';
                if(pow2palin()) countt++;
            }
        }
        for(j=100;j<=999;j++)
        {
            sprintf(str,"%d",j);
            str[3]=str[2];
            str[4]=str[1];
            str[5]=str[0];
            str[6]='\0';
            if(pow2palin()) countt++;

            sprintf(str,"%d",j);
            str[4]=str[2];
            str[5]=str[1];
            str[6]=str[0];
            str[7]='\0';
            for(k=0;k<=9;k++)
            {
                str[3]=k-0+'0';
                if(pow2palin()) countt++;
            }
        }

        printf("Case #%d: %d\n",i+1,countt);
    }
    scanf(" ");
}
