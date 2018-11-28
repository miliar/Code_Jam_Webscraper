#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<queue>
#include<map>
#include<set>

using namespace std;

typedef long long ll;

char str[1010];

int main()
{
//    freopen("1.txt","r",stdin);
//    freopen("2.out","w",stdout);
    int T,n,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%s",&n,str);
        if(n==0)
        {
            printf("Case #%d: 0\n",cas++);
            continue;
        }
        int ans = 0;
        int x = str[0]-'0';
        for(int i=1;i<=n;i++)
        {
            if(str[i]=='0') continue;
            if(x>=i)
                x+=str[i]-'0';
            else
            {
                ans += i-x;
                x = i+str[i]-'0';
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
