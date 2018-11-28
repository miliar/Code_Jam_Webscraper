#include <iostream>
#include <stdio.h>
using namespace std;

void flipabove(char *a,char *p)
{
    if(*a=='+')
        *a='-';
    else
        *a='+';
    if(a==p)
    return;
    flipabove(a-1,p);

}
int recflip(char *a,int &scount,char *p)
{
    //printf("%c\n",*a);
    if(*a=='\0')
        return 0;
    recflip(a+1,scount,p);
    if(*a=='-')
    {
        *a='+';
        scount++;
        flipabove(a-1,p);
    }
}

int main()
{
    #ifndef GOOGLE_CODE_JAM
    freopen("B-large.in","r",stdin);
    freopen("output_file_name.out","w",stdout);
    #endif
    int T;
    scanf("%d",&T);
    int ansT[T];
    for(int test=0;test<T;test++)
    {
    int count=0;
    char a[100];
    scanf("%s",a);
    recflip(a,count,a-1);
    ansT[test]=count;
    }
   for(int ansi=0;ansi<T;ansi++)
    {
    printf("Case #%d: %d\n",ansi+1,ansT[ansi]);
    }
    return 0;
}
