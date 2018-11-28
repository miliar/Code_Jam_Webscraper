#include<bits/stdc++.h>
using namespace std;
bool a[10];
#define MAX 1000000009
bool check()
{
    for(int i=0;i<10;i++)
    {
        if(a[i]==false)
            return false;
    }
    return true;
}
void digits(int n)
{
    int d;
    while(n>0)
    {
        d=n%10;
        a[d]=true;
        n/=10;
    }
}
int main()
{
    int t,n,c,k,i;
    scanf("%d",&t);
    for(c=1;c<=t;c++)
    {
        scanf("%d",&n);
        k=n;i=0;
        memset(a,false,sizeof(a));
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",c);
            continue;
        }
        while(1)
        {
            digits(k);
            if(k>MAX||i>100000)
            {
                printf("Case #%d: INSOMNIA\n",c);
                break;
            }
            if(check()==false)
            {
                i++;
                k+=n;
            }
            else if(check())
            {
                printf("Case #%d: %d\n",c,k);
                break;
            }
        }
    }
    return 0;
}
