#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
        int t,i,j,k,flag=0;
        FILE* in;
        FILE* out;
        in=fopen("B-small-attempt0.in","r");
        out=fopen("OUTPUT.txt","w");
        char s[100];
        char str[100];
        fscanf(in,"%d",&t);
        int count;
        for(i=1;i<=t;i++)
        {
                count=0;
                fscanf(in,"%s",s);
                flag=0;
                while(flag==0)
                {
                        for(j=0;j<strlen(s);j++)
                        {
                                if(s[j]!='+')
                                        break;
                        }
                        if(j==strlen(s))
                        {
                                flag=1;
                                break;
                        }
                        k=0;
                        for(j=1;j<strlen(s);j++)
                        {
                           if(s[k]!=s[j])
                           {
                                break;
                           }
                        }
                        for(k=0;k<j;k++)
                        {
                                if(s[k]=='-')
                                        s[k]='+';
                                else
                                        s[k]='-';
                        }
                        count++;
                }
                fprintf(out,"Case #%d: %d\n",i,count);
        }
}
