#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
    int n,i,s=0,r=0;
    char ch;
    cin>>n;
    int a[n+1];
    ch=getchar();
    for(i=0;i<n+1;i++)
    {
        ch=getchar();
        a[i]=ch-'0';
    }
    s=a[0];
    for(i=1;i<n+1;i++)
    {
        if(s>=i)
        {
            s+=a[i];
        }
        else
        {
            r+=(i-s);
            s+=(i-s);
            s+=a[i];
        }
    }
    printf("Case #%d: %d\n",j,r);
    }
    return 0;
}
