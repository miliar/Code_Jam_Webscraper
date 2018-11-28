#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;
char site[10000];
int main()
{
    int T;cin>>T;
    for(int TT = 1;TT<=T;TT++)
    {
        int n;cin>>n;
        cin>>site;
        int ans = 0;
        int cnt = 0;
        for (int i = 0; i <= n; ++i)
        {
            //cout<<cnt<<" "<<i<<endl;
            if(cnt<i)
            {
                ans += i-cnt;
                cnt += i-cnt+site[i]-'0';
            }
            else cnt += site[i]-'0';
        }
        printf("Case #%d: %d\n",TT,ans );
    }
    return 0;
}