#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define ms(x,y) memset(x,y,sizeof(x))
#define fr(i,x,y) for(int i=x;i<=y;i++)
int n;

void doit()
{
    scanf("%d",&n);
    if (n==0) {puts("INSOMNIA"); return;}
    int now=0,y,x=0;
    while (now!=1023)
    {   x+=n;
        y=x;
        while (y)
        {
            now|= (1<<(y%10));
            y/=10;
        }

    }
    printf("%d\n",x);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {   printf("Case #%d: ",++i);
        doit();
    }
}
/*

5
111111
112112
123231
131313
133311
*/
