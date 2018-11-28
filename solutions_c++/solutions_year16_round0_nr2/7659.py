
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
const int maxn= 105;

using namespace std;

char s[maxn];
int a[maxn];

int len;
int ans;

int main()
{
    int cas=1;
    int i;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    while(T--)
        {
            scanf("%s",s);
            len=strlen(s);
            for(i=0;i<len;i++)
                {
                    if(s[i]=='+') a[i]=1;
                    else a[i]=0;
                }
            a[len]=1;
            ans=0;
            for(i=0;i<len;i++)
                {
                    if(a[i]!=a[i+1]) ans++;
                }
            printf("Case #%d: %d\n",cas++,ans);
        }
    return 0;
}
