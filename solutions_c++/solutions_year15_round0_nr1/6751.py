#include <iostream>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

using namespace std;

int main()
{
        FILE*f=fopen("A-large.in","r");
    FILE*f2=fopen("a.out","w");

    int t,s,temp,req;
    fscanf(f,"%d",&t);

    int k,i;
    for(k=0;k<t;k++){
        temp=0;req=0;
        fscanf(f,"%d",&s);
        char c[s+2];
        fscanf(f,"%s",c);
        for(i=0;i<s+1;i++){
            if(c[i]=='0')continue;
            if(i>temp){req=req+(i-temp);temp=temp+(i-temp);}
            temp += (int)(c[i]-'0');
        }
        fprintf(f2,"Case #%d: %d\n",k+1,req);
    }
    return 0;
}
