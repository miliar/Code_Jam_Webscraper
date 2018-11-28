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
int mp[105][105];
int T,n,m;
int check(int a,int b)
{
    bool flag=true;
	bool in=false;
    int cnt=0;
    FOR(i,0,n)
    {
        if(mp[i][b]==mp[a][b]) cnt++;
        if(mp[i][b] > mp[a][b]) {flag=false;break;}
    }
    if(!flag)
    {
		in=true;
        cnt=0;
        FOR(i,0,m)
        {
            if(mp[a][i]==mp[a][b]) cnt++;
            if(mp[a][i] > mp[a][b]) break;
        }
        if(cnt == m)    flag=true;
    }
    if(flag)
    {
        if(cnt == m&&in)
            return 0;
        return 1;
    }
    else
        return -1;
}
int main(int argc,char* argv[])
{
    std::ios::sync_with_stdio(false);
    scanf("%d",&T);
    FOR(p,1,T+1)
    {
        scanf("%d%d",&n,&m);
        FOR(i,0,n)
        {
            FOR(j,0,m)
            {
                scanf("%d",&mp[i][j]);
            }
        }
        bool flag=true;
        int tmp;
        FOR(i,0,n)
        {
            FOR(j,0,m)
            {
                tmp=check(i,j);
                if(tmp == -1){flag=false;break;}
                if(tmp == 0)    break;
            }
            if(!flag)   break;
        }
        printf("Case #%d: %s",p,flag?"YES\n":"NO\n");
    }
	return 0;
}
