#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
using namespace std;
const int maxn = 1010;
int main()
{
    #ifdef LOCAL
        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);
    #endif // LOCAL
    int ncase;
    scanf("%d",&ncase);
    for(int Tcase = 1 ; Tcase <= ncase ; Tcase ++)
    {
        int smax;
        string str;
        cin>>smax>>str;
        int vec[maxn];
        memset(vec,0,sizeof(vec));
        for(int i = 0 ;i < smax+1 ; i++)
        {
            vec[i] = str[i] - '0';
        }
        int ans = 0;
        for(int i = 1 ; i < smax + 1 ; i++)
        {
            vec[i] += vec[i-1];
        }

        for(int i = 1;i < smax + 1 ; i++)
        {
            if( ( vec[i-1] + ans ) < i)
            {
                ans += ( i - vec[i-1] - ans);
            }
        }
        printf("Case #%d: %d\n",Tcase,ans);
    }
    return 0;
}
