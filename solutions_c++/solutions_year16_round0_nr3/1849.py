#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<cstdlib>
using namespace std;
int N,J;
int hash[10];
char s[1010];
int f[110][2];
int a[110];
int b[110];
int is_not_prime(int p)
{
    for (int i=2;i<=100;i++)
    {
        int res=0;
        int pow=1;
        for (int j=0;j<N;j++)
        {
            if (a[j]) res=(res+pow)%i;
            pow=pow*p%i;
        }
        if (res==0)
        {
            return i;
        }
    }
    return 0;
}
bool ok()
{
    for (int i=2;i<=10;i++)
    {
        b[i]=is_not_prime(i);
        if (b[i]==0)
        {
            return false;
        }
    }
    return true;
}
void work(int idx)
{
    printf("Case #%d:\n",idx);
    scanf("%d%d",&N,&J);
    int cnt=0;
    for (int i=0;i<(1<<N-2);i++)
    {
        a[0]=1;
        a[N-1]=1;
        for (int j=0;j<N-2;j++)
        {
            a[j+1]=(i>>j)&1;
        }
        if (ok())
        {
            cnt++;
            for (int j=N-1;j>=0;j--)
            printf("%d",a[j]);
            for (int j=2;j<=10;j++)
            printf(" %d",b[j]);
            printf("\n");
        }
        if (cnt==J)
        {
            break;
        }
    }
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    work(i);
    return 0;
}
