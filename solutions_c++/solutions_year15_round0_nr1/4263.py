#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cassert>
#include<climits>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
#define INF (1ll<<62)
using namespace std;
char s[10005];
int main()
{
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        int n;
        cin>>n;
        scanf("%s",s);
        int ans=0,sum=0;
        for (int i=0; i<=n; i++)
        {
            if (i-sum>0) ans+=i-sum,sum+=i-sum;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
