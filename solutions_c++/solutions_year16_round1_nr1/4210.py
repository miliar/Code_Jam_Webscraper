#include <iostream>
#include <algorithm>
#include <limits>
#include <iterator>
#include <functional>
#include <stdio.h>
#include <string.h>
#include <cmath>

using namespace std;

void insertatbeg(char a,char *arr,int l)
{
    int i,j,k;
    for(i=l;i>0;i--)
    {
        arr[i]=arr[i-1];
    }
    arr[0]=a;
    arr[l+1]='\0';
}

int main()
{
    FILE *fpi,*fpo;
    fpi=fopen("A-large11.in","r");
    fpo=fopen("write1.out","w");
    int t,T,i,j,k,l,n;
    char a[1002],b[1002],c[1002];
    fscanf(fpi,"%d",&T);
    for(t=1;t<=T;t++)
    {
        fprintf(fpo,"Case #%d: ",t);
        fscanf(fpi,"%s",a);
        l=strlen(a);
        b[0]=a[0];
        b[1]='\0';
        //printf("%d",(int)a[0]);
        if(l!=1)
        {
        j=1;
        for(i=1;i<l;i++)
        {
            if((int)a[i]>=(int)b[0])
            {
                //printf("b");
                insertatbeg(a[i],b,j);
            }
            else
            {
               // printf("e");
                b[j]=a[i];
                b[j+1]='\0';
            }
            j++;
        }
        }
        fprintf(fpo,"%s\n",b);
    }

}
