#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<cstdlib>
using namespace std;
int hash[10];
char s[1010];
int f[110][2];
void work(int idx)
{
    printf("Case #%d: ",idx);
    scanf("%s",s+1);
    int n=strlen(s+1);
    memset(f,120,sizeof(f));
    f[0][0]=0;
    f[0][1]=0;
    for (int i=1;i<=n;i++)
    {
        if (s[i]=='-')
        {
            f[i][0]=f[i-1][0];
            for (int j=i;s[j]=='-';j--)
            {
                f[i][1]=min(f[i][1],f[j-1][0]+1);
            }
        }
        else
        {
            f[i][1]=f[i-1][1];
            for (int j=i;s[j]=='+';j--)
            {
                f[i][0]=min(f[i][0],f[j-1][1]+1);
            }
        }
    }
    printf("%d\n",f[n][1]);
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
