#include <iostream>
#include<stdio.h>
#include <string.h>
char a[3024];
char b[3000];
using namespace std;
int n;
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int first=1001,last=1001;
    scanf("%d",&n);
    for(int u=1;u<=n;u++)
    {
        scanf("%s",a);
        first=1001;
        last=1001;
        b[first]=a[0];
        for(int i=1;i<strlen(a);i++)
        {
            if(a[i]<b[first])
            {
                b[++last]=a[i];
            }
            else
                b[--first]=a[i];
        }
        printf("Case #%d: ",u);
        for(int i=first;i<=last;i++)
            printf("%c",b[i]);
        printf("\n");

    }
    return 0;
}
