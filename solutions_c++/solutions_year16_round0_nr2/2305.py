#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;
#define maxn 500
char s[maxn];
vector<int>g;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        g.clear();
        scanf("%s",s);
        int len=strlen(s);
        for(int i=0;i<len;i++)
        {
            if(i!=0&&s[i]==s[i-1]) continue;
            if(s[i]=='+') g.push_back(1);
            else g.push_back(0);
        }
        int ans=g.size()-1;
        if(g[g.size()-1]==0) ans++;
        printf("Case #%d: %d\n",cas,ans);
    }
}
