#include<cstdio>
#include<cmath>
using namespace std;
int n,m;
int a[20],b[20];
void check()
{
    long long x,i,j,st;
    for(i=2;i<=10;i++)
    {
        st=1;
        x=0;
        for(j=n;j>=1;j--)
        {
            x+=st*(long long)a[j];
            st*=i;
        }
        b[i]=0;
        for(j=2;j<=sqrt(x);j++)
            if(x%j==0)
            {
                b[i]=j;
                break;
            }
        if(!b[i])return;
    }
    for(i=1;i<=n;i++)
        printf("%d",a[i]);
    for(i=2;i<=10;i++)
        printf(" %d",b[i]);
    printf("\n");
    m--;
}
void rec(int k)
{
    if(!m)return;
    if(k==n)
    {
        a[k]=1;
        check();
        return;
    }
    a[k]=1;
    rec(k+1);
    a[k]=0;
    rec(k+1);
}
int main()
{
    int i,t;
    scanf("%d",&t);
    scanf("%d%d",&n,&m);
    printf("Case #1: \n");
    a[1]=1;
    rec(2);
}
