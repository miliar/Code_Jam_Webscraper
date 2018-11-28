#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
#define sqr(x) ((x)*(x))
#define LL long long
#define eps 1e-9
#define INF 0x7fffffff
#define pi acos(-1.0);
#define CLR(x,v) memset(x,v,sizeof(x));
#define FOR(i,a,b) for(int i=a;i<b;i++)
int a[105];
bool isrev(int x)
{
    CLR(a,0);
    int cnt=0;
    while(x)
    {
        a[cnt++]=x%10;
        x/=10;
    }
    for(int i=0;i<cnt/2;i++)
        if(a[i]!=a[cnt-i-1])    return false;
    return true;
}

int main(int argc,char* argv[])
{
    std::ios::sync_with_stdio(false);
    int T;
    int n,m;
    scanf("%d",&T);
    FOR(p,1,T+1)
    {
        int res=0;
        scanf("%d%d",&n,&m);
        for(int i=n;i<=m;i++)
        {
            if(isrev(i))
            {
                double tmp=sqrt(i);
                if(tmp == (int)tmp)
                {
                    if(isrev(tmp))
                        res++;
                }
            }
        }
        printf("Case #%d: %d\n",p,res);
    }
	return 0;
}

