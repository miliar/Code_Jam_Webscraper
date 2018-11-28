#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<queue>
#include<vector>
#include<time.h>
using namespace std;
char s[10005];
int cnt[10005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        memset(cnt,0,sizeof(cnt));
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int ans=0,now=0,res=0;
        for(int i=0;s[i];++i)
        {
            cnt[i]=s[i]-'0';
            if(!cnt[i])
                continue;
            if(i>ans)
                ans+=i-now,now=i;
            now+=cnt[i];
            res=max(res,ans);
        }
        printf("Case #%d: %d\n",++ca,res);


    }
}
