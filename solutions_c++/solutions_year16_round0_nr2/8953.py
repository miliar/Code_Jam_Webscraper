#include<bits/stdc++.h>
#define INT long long int
using namespace std;

int main()
{
    FILE *fp,*fq;
    fp=fopen("B-large.in","r");
    fq=fopen("output.txt","w");
    INT caseno=0,t,i,j,l,flag,flag1,flag2,a,b,n;
    char str[200];
    fscanf(fp,"%lld",&t);
    while(t--)
    {
        fscanf(fp,"%s",str);
        flag1=flag2=0;
        for(i=0;str[i]!='\0';i++)
        {
            if(str[i]=='+')
                flag1=1;
            if(str[i]=='-')
                flag2=1;
        }
        fprintf(fq,"Case #%lld: ",++caseno);
        n=0;
        if(flag2==0)
            fprintf(fq,"0\n");
        else if(flag1==0)
            fprintf(fq,"1\n");
        else if(str[0]=='-')
        {
            n=0;
            for(i=0;str[i]!='\0';i++)
            {
                if(str[i]=='-' && str[i+1]=='+')
                    n++;
            }
            if(str[i-1]=='-')
                n++;
            fprintf(fq,"%lld\n",2*n-1);
        }
        else if(str[0]=='+')
        {
            n=0;
            for(i=0;str[i]!='\0';i++)
            {
                if(str[i]=='+' && str[i+1]=='-')
                    n++;
            }
            fprintf(fq,"%lld\n",2*n);
        }
    }
    return 0;
}
