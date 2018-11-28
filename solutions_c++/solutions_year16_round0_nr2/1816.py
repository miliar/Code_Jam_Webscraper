#include <iostream>
#include<stdio.h>
#include<string>

using namespace std;

int main()
{
    FILE* in=fopen("b-large.in","r");
    FILE* out=fopen("b-large.out","w");
    int T;
    fscanf(in,"%d",&T);
    for(int num=1;num<=T;num++)
    {
        char s[200];
        fscanf(in,"%s",&s);
        int n=0;
        while(s[n]) n++;
        int kol=0;
        int i=0;
        if(s[0]=='+')
        {
            bool fl=false;
            for(int j=1;j<n && !fl;j++) if(s[j]=='-') fl=true;
            if(fl) kol++;
        }
        while(i<n)
        {
            if(s[i]=='-')
            {
                kol++;
                while(i<n && s[i]=='-') i++;
                if(i<n)
                {
                    bool fl=false;
                    for(int j=i;j<n && !fl;j++) if(s[j]=='-') fl=true;
                    if(fl) kol++;
                }
            }
            else i++;
        }
        fprintf(out,"Case #%d: %d\n",num,kol);
    }
    return 0;
}
