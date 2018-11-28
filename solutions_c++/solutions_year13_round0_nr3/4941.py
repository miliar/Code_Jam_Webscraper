#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

bool Judge(int x)
{
    int tmp=x;
    int y=0;
    while(tmp)
    {
       y*=10;
       y+=tmp%10;
       tmp/=10;
    }
    if(x!=y)
        return false;
    int a=sqrt(x*1.0);
    if(a*a!=x)
        return false;
    int b=0;
    int t=a;
    while(t)
    {
        b*=10;
        b+=t%10;
        t/=10;
    }
    if(a!=b)
        return false;
    return true;
}

int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int cases,id=1;
    scanf("%d",&cases);
    while(cases--)
    {
        printf("Case #%d: ",id++);
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for(int i=a;i<=b;i++)
            if(Judge(i))
                ans++;
        printf("%d\n",ans);
    }
    return 0;
}
