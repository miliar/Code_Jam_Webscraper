#include <stdio.h>
#include <stdlib.h>
long long a[10000005];
int string[100];
int main()
{
    long long temp;
    int p=0;
    for(int i=1;i<=100000000;i++)
    {
        int j;
        long long temp2;
        for(temp2=i,j=0;temp2>0;j++)
        {
            string[j]=temp2%10;
            temp2/=10;
        }
        j--;
        int no=0;
        for(int q=0;q<j;q++,j--)
        {
            if(string[q]!=string[j])
            {
                no=1;
            }
        }
        if(no)
        {
            continue;
        }


        temp=(long long)i*i;
        //printf("%I64d\n",temp);

        for(temp2=temp,j=0;temp2>0;j++)
        {
            string[j]=temp2%10;
            temp2/=10;
        }
        j--;
        no=0;
        for(int q=0;q<j;q++,j--)
        {
            if(string[q]!=string[j])
            {
                no=1;
            }
        }
        if(!no)
        {
            a[p++]=temp;
        }
    }
    /*for(int i=0;i<100;i++)
    {
        printf("%I64d\n",a[i]);
    }*/
    //system("pause");
    FILE *in=fopen("C-large-1.in","r");
    FILE *out=fopen("output.txt","w");
    int total;
    int count;
    long long from,to;
    fscanf(in,"%d",&total);
    for(int o=0;o<total;o++)
    {
        fscanf(in,"%I64d %I64d",&from,&to);
        count=0;
        for(int j=0;j<p;j++)
        {
            if(from<=a[j] && a[j]<=to)
            {
                count++;
            }
        }
        fprintf(out,"Case #%d: %d\n",o+1,count);
    }
    return 0;
}
