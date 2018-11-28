#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define maxn 200005
char s[1005];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int val;
        scanf("%d",&val);
        scanf("%s",s);
        int len=strlen(s);
        int all=0;
        int temp=0;
        for(int i=0;i<len;i++)
        {
            if(s[i]=='0')   continue;
            if(all<i)
            {
                temp+=i-all;
                all+=i-all+s[i]-'0';
            }
            else all+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cas,temp);
    }
}
