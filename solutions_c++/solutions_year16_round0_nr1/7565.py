
#include <string.h>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <fstream>
#define  LL long long
#define MOD 1000000007

using namespace std;

bool vis[10];

LL N;
int T;
int cnt;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int i=1;
    scanf("%d",&T);
    while(T--)
        {
            memset(vis,false,sizeof(vis));
            scanf("%lld",&N);
            if(N==0) {printf("Case #%d: INSOMNIA\n",i++);continue;}
            cnt=0;
            LL tmp=N;
            LL mm;
            while(tmp>0)
                {
                    mm=tmp%10;
                    if(!vis[mm]) {vis[mm]=true;cnt++;}
                    tmp/=10;
                }
               LL ans=N;
            while(cnt<10)
                {
                    ans+=N;
                    tmp=ans;
                    while(tmp>0)
                {
                    mm=tmp%10;
                    if(!vis[mm]) {vis[mm]=true;cnt++;}
                    tmp/=10;
                }
                }
            printf("Case #%d: %lld\n",i++,ans);
        }
    return 0;
}

