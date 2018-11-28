#include<iostream>
#include<algorithm>
#include<string.h>
#include<stdio.h>
#define O 0
#define X 1
#define T 2
int c[4];
using namespace std;
int check(char a[5][5])
{
    int i,j,flag=0;
    char ch='T';
    for(i=0;i<4;i++)
   {
       c[X]=0;
       c[O]=0;
       c[T]=0;
    for(j=0;j<4;j++)
    {
        if(a[i][j]=='X')
            c[X]++;
        else if(a[i][j]=='O')
            c[O]++;
        else if(a[i][j]=='T')
            c[T]++;
        else
            flag=1;
    }
    if(c[X]+c[T]==4)
        return 1;
    else if(c[O]+c[T]==4)
        return 2;
   }
   for(j=0;j<4;j++)
   {
       c[X]=0;
       c[O]=0;
       c[T]=0;
    for(i=0;i<4;i++)
    {
        if(a[i][j]=='X')
            c[X]++;
        else if(a[i][j]=='O')
            c[O]++;
        else if(a[i][j]=='T')
            c[T]++;
    }
    if(c[X]+c[T]==4)
        return 1;
    else if(c[O]+c[T]==4)
        return 2;
   }
   c[O]=c[X]=c[T]=0;
   for(i=0;i<4;i++)
   {
       if(a[i][i]=='X')
            c[X]++;
        else if(a[i][i]=='O')
            c[O]++;
        else if(a[i][i]=='T')
            c[T]++;

    if(c[X]+c[T]==4)
        return 1;
    else if(c[O]+c[T]==4)
        return 2;
   }
    c[O]=c[X]=c[T]=0;
   for(i=0;i<4;i++)
   {
       if(a[i][3-i]=='X')
            c[X]++;
        else if(a[i][3-i]=='O')
            c[O]++;
        else if(a[i][3-i]=='T')
            c[T]++;

    if(c[X]+c[T]==4)
        return 1;
    else if(c[O]+c[T]==4)
        return 2;
   }
   if(flag)
    return -1;
   return 0;
}


int main()
{
    int t,i,j;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);

    for(j=1;j<=t;j++)
    {
        char s[5][5];
        for(i=0;i<4;i++)
            scanf("%s",s[i]);

            int k=check(s);
            switch(k)
            {
            case -1:
                printf("Case #%d: Game has not completed\n",j);
                break;

            case 0:
                printf("Case #%d: Draw\n",j);
                break;

            case 1:
                printf("Case #%d: X won\n",j);
                break;

            case 2:
                printf("Case #%d: O won\n",j);
            }


    }
    return 0;
}
