#include <iostream>
#include <stdio.h>
#include <queue>
#include <cmath>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define LL                                      long long
#define scan(a)                             scanf("%d",&a)
#define maxn                                1333
#define REP(i,a,b)                          for(int i=a;i<b;++i)

int t,sm;
char str[maxn];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    int cas=1;
    while(t--)
    {
        scan(sm);
        scanf("%s",&str);
        int ans=0,cnt=str[0]-'0';
        REP(i,1,sm+1)
        {
            int c=str[i]-'0';
            if(cnt>=i)
                cnt+=c;
            else
            {
                ans+=i-cnt;
                cnt=i+c;
            }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
