#include <stdio.h>
#include <stdlib.h>

int j,k,l,m[100],t,z,i;
char s[11];


int task()
{
    m[i]=0;
    for(j=0;j<10;j++)         //testing the number of elements entered
    {
        if(s[j]=='\0')
        break;
    }

    while(1)
    {   for(k=0;k<j;k++)         //first k+1 same
            {
                if(s[k]!=s[k+1])
                break;
            }
            if((s[0]=='+')&&(s[k+1]=='\0')) //testing whether initially all +
            {
                return 0;
            }

       m[i]++;     //if not initializing the counter

            for(l=0;l<k+1;l++)         //flipping
            {
                if(s[k+1]!='\0')
                s[l]=s[k+1];
                if(s[k+1]=='\0')
                s[l]='+';
            }

    }




}

int main()
{

    scanf("%d",&t);//getting the number of test cases
    for(i=0;i<t;i++)//t number of test cases
    {
       scanf("%s",s);
       task();
    }
    for(z=0;z<t;z++)
    {
        printf("Case #%d: %d\n",z+1,m[z]);
    }
    return 0;

    }
