//GCJ 2015Q A
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int sm;
char s[1002];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int Case;
    scanf("%d",&Case);
    for(int t=1;t<=Case;++t)
    {
        scanf("%d%s",&sm,s);
        int cnt=0,sum=s[0]-'0';
        for(int i=1;i<=sm;++i)
        {
            if(s[i]=='0') continue;
            if(sum<i) cnt+=i-sum,sum=i;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
