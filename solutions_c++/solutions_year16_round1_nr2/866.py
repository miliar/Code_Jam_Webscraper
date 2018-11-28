#include <set>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ull;
#define A first
#define B second
#define MP make_pair
#define PB push_back
const int maxn=3000;
int tot[maxn];
vector<int> ans;
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        memset(tot,0,sizeof(tot));
        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                int t;
                scanf("%d",&t);
                ++tot[t];
            }
        }
        ans.clear();
        for(int i=0;i<maxn;i++)
            if(tot[i]&1)
                ans.PB(i);
        sort(ans.begin(),ans.end());
        printf("Case #%d:",cas++);
        for(int i=0;i<n;i++)
            printf(" %d",ans[i]);
        printf("\n");
    }
    return 0;
}
