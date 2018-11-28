#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<vector>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
const int maxn=1010;
int N;
char s[maxn];
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%s",&N,s);
        int ans=0,sum=0;
        for(int i=0;i<=N;i++)
        {
            if(i>sum)
                ans+=i-sum,sum=i;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
