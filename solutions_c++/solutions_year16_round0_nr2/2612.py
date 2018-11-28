#include <iostream>
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
int n;
char a[1024];
int t;
void revers(int u)
{
    for(int i=0;i<=u/2;i++)
        swap(a[i],a[u-i]);
    for(int i=0;i<=u;i++)
        a[i]^=6;
}
int sorteaza(int n)
{
    int u=0,k=0;
    while(n>=0&&a[n]=='+')
        n--;
    if(n<0)
        return 0;

    while(u<n&& a[u]=='+')
        u++;
       // a[n+1]='\0';
       u--;
    if(u>=0)
    {
        revers(u);
        k=1;
    }
    revers(n);
    return 1+k+sorteaza(n);
}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);


    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%s",a);
        n=strlen(a);
        printf("Case #%d: %d\n",i,sorteaza(n-1));
    }
//    a[0]='+';
//    printf("%c ",a[0]);
//    a[0]^=6;
//    printf("%c ",a[0]);
    return 0;
}
