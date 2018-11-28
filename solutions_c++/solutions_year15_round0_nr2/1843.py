#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
using namespace std;
int pi[10010];
int main()
{
    int T; cin >> T;
    for (int TT = 1 ; TT <= T; TT++)
    {
        int n;cin>>n;
        int maxnum = 0;
        int sum = 0;
        for (int i = 0; i < n; ++i)
        {
            scanf("%d",pi+i);
            maxnum = max(maxnum,pi[i]);
            sum += max(maxnum,pi[i]);
        }
        // /cout<<maxnum<<endl;
        sort(pi,pi+n,greater<int>());
        int ans = 1e9;
        for (int i = 1; i <= maxnum; ++i)
        {
            int tmp = 0;
            for (int j = 0; j < n; ++j)
            {
                if(pi[j]>i) tmp += ceil((pi[j]-i)*1.0/i);
            }
            //printf("tmp: %d i: %d\n",tmp,i);
            ans = min(ans,tmp+i);
        }
        printf("Case #%d: %d\n",TT,ans);
    }
    return 0;
}