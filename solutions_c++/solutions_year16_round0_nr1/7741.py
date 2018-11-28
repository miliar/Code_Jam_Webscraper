//GCJ 2015Q A
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int N;
bool m[10];
int cnt;
bool solve(int x)
{
    while(x>0)
    {
        int d=x%10;
        if(m[d]==0) m[d]=1,cnt++;
        x/=10;
    }
    if(cnt==10) return true;
    else return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Case;
    scanf("%d",&Case);
    for(int t=1;t<=Case;++t)
    {
        scanf("%d",&N);
        cnt=0;
        int x=0;
        memset(m,0,sizeof(m));
        if(N!=0)
        {
            for(int i=1;;++i)
            if(solve(N*i))
            {
                x=N*i;
                break;
            }
            printf("Case #%d: %d\n",t,x);
        }
        else
            printf("Case #%d: INSOMNIA\n",t);
    }
    return 0;
}
