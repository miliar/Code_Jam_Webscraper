#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    freopen("output.out","w",stdout);
    char num[1111];
    int T;
    cin >>  T;
    for (int t=1; t<=T; t++)
    {
        int mx,cnt=0;
        int ans=0;
        scanf("%d %s",&mx,num);
        for (int j=0; j<mx; j++)
        {
            cnt+=num[j]-'0';
            if (j+1-cnt>ans)
                ans=j+1-cnt;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}