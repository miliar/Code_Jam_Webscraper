#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
int ans[10000005];

bool right(char * ch)
{
     int i,j;
     i = 0;j = strlen(ch)-1;
     while (i<j)
     {
           if (ch[i]!=ch[j]) return false;
           ++i;--j;
     }
     return true;
}

int main()
{
    memset(ans,0,sizeof(ans));
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    for (int i =1;i<=10000000;++i)
    {
        long long j = i * i;
        char ch[1000];
        char ch1[1000];
        memset(ch,0,sizeof(ch));
        memset(ch1,0,sizeof(ch1));
        _i64toa(j,ch,10);
        _itoa(i,ch1,10);
        if (right(ch)&&right(ch1)) {ans[i]=ans[i-1]+1;}
        else ans[i]=ans[i-1];
    }
    int t;
    scanf("%d",&t);
    int t1=1;
    int a,b;
    while (t--)
    {
          scanf("%d %d",&a,&b);
          int x = sqrt(a);int y = sqrt(b);
          if (x*x == a) --x;
          printf("Case #%d: %d\n",t1,ans[y]-ans[x]);
          t1++;
    }
}
