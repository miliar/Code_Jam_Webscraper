#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define ms(x,y) memset(x,y,sizeof(x))
#define fr(i,x,y) for(int i=x;i<=y;i++)
int n;
#define N 105
char str[N];

void doit()
{
    scanf("%s",str+1);
    int len=strlen(str+1);
    int x=len,ans=0;
    while (x>=1)
    {
        if (str[x]=='+')
        {
            x--;
            continue;
        }
        for(int i=1;i<=x;i++)
            if (str[i]=='+')str[i]='-';else str[i]='+';
        ans++;
        x--;
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {   printf("Case #%d: ",++i);
        doit();
    }
}
/*

5
-
-+
+-
+++
--+-

*/
