#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
    int t,q=1;
    FILE *fptr,*fptr1;
    fptr1=fopen("output.in","w");
if((fptr=fopen("input.in","r"))!=NULL)
{
    fscanf(fptr,"%i",&t);

        while(q<=t)
    {
        char a[1000],b[1000];
        int num,i,j=0,k;
        fscanf(fptr,"%s",a);
        num=strlen(a);
        b[0]=a[0];
        for(i=1;i<num;i++)
        {
            j++;
            if(b[0]<=a[i])
            {
                for(k=j;k>0;k--)
                {
                b[k]=b[k-1];
                }
                b[0]=a[i];
            }
            else
            {
                b[j]=a[i];
            }
        }
        b[++j]='\0';
        fprintf(fptr1,"Case #%li: %s\n",q,b);
        q++;
   }
}
fclose(fptr);
fclose(fptr1);
    return 0;
}

