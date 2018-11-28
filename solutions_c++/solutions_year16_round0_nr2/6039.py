#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
char c[1011];
int T;
int n;
int a[1011];
int b[1011];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Blarge.txt","w",stdout);
    int i,j,k;
    int p,q,r;
scanf("%d",&T);
for(int ii=0;ii<T;ii++)
{
    scanf("%s",c);
    n = strlen(c);
    r=0;
    for(i=0;i<n;i++)
    {
        if(c[i]=='-')a[i]=0;
        else if(c[i]=='+')a[i]=1;
    }
    k=1;
    for(i=n-1;i>=0;i--)
    {
        if(a[i]!=k)
        {
            k++;
            k%=2;
            r++;
        }
    }



    printf("Case #%d: ",ii+1);
    printf("%d\n",r);
}


    return 0;
}

