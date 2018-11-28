#include<iostream>
#include<stdio.h>
#include<strings.h>

using namespace std;

int main()
{
    FILE *fp=fopen("A-large.in","r");
    int tc;
    int a=1;
    fscanf(fp,"%d\n",&tc);
    for(a=1;a<=tc;a++)
    {
        int smax;
        char str[1007];
        bzero(str,1007);
        fscanf(fp,"%d %s\n",&smax,str);
        int i,j;
        int value=0;
        int values[1007]={0};

        values[0]=str[0]-'0';

        for(i=1;i<=smax;i++)
        {
            values[i]=values[i-1]+str[i]-'0';
        }

        for(i=0;i<=smax;i++)
        {
            if(values[i]<i+1)
            {
                value++;
                for(j=i;j<=smax;j++)
                {
                    values[j]+=1;
                }
            }
        }
        FILE *fp1;
        fp1=fopen("A-large.out","a");
        fprintf(fp1,"Case #%d: %d\n",a,value);
        fclose(fp1);
    }
    fclose(fp);
    return 0;
}
