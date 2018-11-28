#include<iostream>
#include<stdio.h>
#include<strings.h>

using namespace std;

int main()
{
    FILE *fp=fopen("input","r");
    int tc;
    int k;
    fscanf(fp,"%d",&tc);
    //scanf("%d",&tc);
    for(k=1;k<=tc;k++)
    {
        int smax;
        char str[1002];
        char str1[1002];
        bzero(str,1002);
        bzero(str1,1002);
        fscanf(fp,"%d %s\n",&smax,str);
        int i,j;
        int c=0;

        str1[0]=str[0]-'0';

        for(i=1;i<=smax;i++)
        {
            str1[i]=str1[i-1]+str[i]-'0';
        }

        for(i=0;i<=smax;i++)
        {
            if(str1[i]<i+1)
            {
                c++;
                for(j=i;j<=smax;j++)
                {
                    str1[j]+=1;
                }
            }
        }
        FILE *fp1;
        fp1=fopen("out","a");
        fprintf(fp1,"Case #%d: %d\n",k,c);
        fclose(fp1);
    }
    fclose(fp);
    return 0;
}
