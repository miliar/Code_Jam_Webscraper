#include<stdio.h>
#include<sstream>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
    int t,y,a[100],k,j,l,b,count;
    char s[100];
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%s",s);
        y=strlen(s);

        for(j=0;j<y;j++)
        {
            if(s[j]==43)
            a[j]=1;
            else
            a[j]=0;
        }
        for(count=0;;count++)
        {
            if(a[0]==1)
            {
                for(k=0;(k<y-1)&&(a[k+1]==1);k++);
                if(k==(y-1))
                break;
            }
            else
            {
                for(k=y-1;(k>=0)&&(a[k]==1);k--,y--);
            }

            for(j=0,l=k;j<=l;j++,l--)
            {
                b=1-a[j];
                a[j]=1-a[l];
                a[l]=b;
            }

         }

        printf("Case #%d: %d\n",i,count);
    count=0;
    }

    return 0;
}

