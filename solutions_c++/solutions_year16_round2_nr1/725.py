#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <bitset>
#include <map>

using namespace std;

#define MAXN 2100
#define INF 0x3f3f3f3f
#define mo 1000000007
typedef long long LL;

int n,cnt[30],ans[30];
char s[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    ///freopen("A-large.out","w",stdout);
    int i,j,k,t;
    for(scanf("%d",&t),i=1;i<=t;++i){
        memset(cnt,0,sizeof(cnt));
        memset(ans,0,sizeof(ans));
        scanf("%s",s); n=strlen(s);
        for(j=0;j<n;++j) ++cnt[s[j]-'A'];
        k=cnt['Z'-'A']; ans[0]+=k;
        cnt['Z'-'A']-=k; cnt['E'-'A']-=k; cnt['R'-'A']-=k; cnt['O'-'A']-=k;
        k=cnt['U'-'A']; ans[4]+=k;
        cnt['F'-'A']-=k; cnt['O'-'A']-=k; cnt['U'-'A']-=k; cnt['R'-'A']-=k;
        k=cnt['X'-'A']; ans[6]+=k;
        cnt['S'-'A']-=k; cnt['I'-'A']-=k; cnt['X'-'A']-=k;
        k=cnt['G'-'A']; ans[8]+=k;
        cnt['E'-'A']-=k; cnt['I'-'A']-=k; cnt['G'-'A']-=k; cnt['H'-'A']-=k; cnt['T'-'A']-=k;
        k=cnt['H'-'A']; ans[3]+=k;
        cnt['T'-'A']-=k; cnt['H'-'A']-=k; cnt['R'-'A']-=k; cnt['E'-'A']-=k; cnt['E'-'A']-=k;
        k=cnt['T'-'A']; ans[2]+=k;
        cnt['T'-'A']-=k; cnt['W'-'A']-=k; cnt['O'-'A']-=k;
        k=cnt['F'-'A']; ans[5]+=k;
        cnt['F'-'A']-=k; cnt['I'-'A']-=k; cnt['V'-'A']-=k; cnt['E'-'A']-=k;
        k=cnt['S'-'A']; ans[7]+=k;
        cnt['S'-'A']-=k; cnt['E'-'A']-=k; cnt['V'-'A']-=k; cnt['E'-'A']-=k; cnt['N'-'A']-=k;
        k=cnt['O'-'A']; ans[1]+=k;
        cnt['O'-'A']-=k; cnt['N'-'A']-=k; cnt['E'-'A']-=k;
        k=cnt['I'-'A']; ans[9]+=k;
        cnt['N'-'A']-=k; cnt['I'-'A']-=k; cnt['N'-'A']-=k; cnt['E'-'A']-=k;
        printf("Case #%d: ",i);
        for(j=0;j<10;++j) for(k=1;k<=ans[j];++k) printf("%d",j);
        printf("\n");
    }
    return 0;
}
