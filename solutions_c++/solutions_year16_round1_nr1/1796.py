#include <iostream>
#include<stdio.h>
#include<string.h>
#include<limits.h>
using namespace std;
char s[10000];
int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,c=1;
    scanf("%d",&t);
    while(t--)
    {
        char a[10000];
        printf("Case #%d: ",c);
        c++;
        scanf("%s",&s);
        int maxx=INT_MIN;
        int l=strlen(s),pos;
        for(int i=0; i<l; i++)
        {
            if(s[i]>maxx)
            {
                maxx=s[i];
                pos=i;
            }
            //maxx=max(maxx,s[i]);
        }
        //j=l/2;
        a[l]=s[0];
        int ll,rr;
        ll=l;
        rr=l;
        for(int i=1; i<l; i++)
        {
            if(s[i]>=a[ll])
            {
                a[--ll]=s[i];
            }
            else if(s[i]<a[ll])
            {
                a[++rr]=s[i];
            }
        }
        for(int i=ll; i<=rr; i++)
        {
            printf("%c",a[i]);
        }
        printf("\n");

    }
    return 0;
}
