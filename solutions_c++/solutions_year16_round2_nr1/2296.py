//GCJ 2016 round1B A
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#define MAXL 2005
#define MAXN 1005
using namespace std;
char s[MAXL];
int cnt[26];
int ans[10];

void re()
{
    if(cnt[25]>0)
    {
        ans[0]+=cnt[25];
        cnt[4]-=cnt[25];
        cnt[14]-=cnt[25];
        cnt[17]-=cnt[25];
        cnt[25]=0;
    }
    if(cnt[22]>0)
    {
        ans[2]+=cnt[22];
        cnt[19]-=cnt[22];
        cnt[14]-=cnt[22];
        cnt[22]=0;
    }
    if(cnt[23]>0)
    {
        ans[6]+=cnt[23];
        cnt[8]-=cnt[23];
        cnt[18]-=cnt[23];
        cnt[23]=0;
    }
    if(cnt[18]>0)
    {
        ans[7]+=cnt[18];
        cnt[4]-=2*cnt[18];
        cnt[21]-=cnt[18];
        cnt[13]-=cnt[18];
        cnt[18]=0;
    }
    if(cnt[21]>0)
    {
        ans[5]+=cnt[21];
        cnt[4]-=cnt[21];
        cnt[8]-=cnt[21];
        cnt[5]-=cnt[21];
        cnt[21]=0;
    }
    if(cnt[5]>0)
    {
        ans[4]+=cnt[5];
        cnt[14]-=cnt[5];
        cnt[20]-=cnt[5];
        cnt[17]-=cnt[5];
        cnt[5]=0;
    }
    if(cnt[17]>0)
    {
        ans[3]+=cnt[17];
        cnt[19]-=cnt[17];
        cnt[7]-=cnt[17];
        cnt[4]-=2*cnt[17];
        cnt[17]=0;
    }
    if(cnt[7]>0)
    {
        ans[8]+=cnt[7];
        cnt[4]-=cnt[7];
        cnt[8]-=cnt[7];
        cnt[6]-=cnt[7];
        cnt[19]-=cnt[7];
        cnt[7]=0;
    }
    if(cnt[8]>0)
    {
        ans[9]+=cnt[8];
        cnt[13]-=2*cnt[8];
        cnt[4]-=cnt[8];
        cnt[8]=0;
    }
    if(cnt[4]>0)
    {
        ans[1]+=cnt[4];
    }
}
void solve()
{
    memset(cnt,0,sizeof(cnt));
    memset(ans,0,sizeof(ans));
    int len = strlen(s);
    for(int i=0;i<len;++i)
    {
        cnt[s[i]-'A']++;
    }
    re();
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Case;
    scanf("%d",&Case);
    for(int t=1;t<=Case;++t)
    {
        scanf("%s",s);
        solve();
        printf("Case #%d: ",t);
        for(int i=0;i<=9;++i)
        {
            if(ans[i]>0)
            {
                for(int j=0;j<ans[i];++j)
                    printf("%d",i);
            }
        }
        printf("\n");
    }
    return 0;
}
