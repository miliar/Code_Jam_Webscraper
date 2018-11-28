#include <iostream>
#include <cstdio>
#include <set>
#include <string>
#include <string.h>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cctype>
#include <algorithm>
#include <sstream>
#define mt(a) memset(a,0,sizeof a)
#define fl(a,b,c) fill(a,b,c)
#define pii pair<int,int>
#define INF 1000000000+7
#define MAXN 1e18
#define iin(x) scanf("%d",&x)
#define complete_unique(x) x.erase(unique(x.begin(),x.end()),x.end())
using namespace std;
typedef long long ll;

int main()
{
    //freopen("A-large.in","r",stdin);
   // freopen("A-large.out","w",stdout);
    int t,cas = 1;
    cin >> t;
    while(t--)
    {
        ll n,now = 0;
        cin >> n;
        printf("Case #%d: ",cas++);
        int cnt = 0,sum = 0;
        map<int,int>vis;
        while(cnt < INF && now < MAXN && sum < 10)
        {
            cnt++;
            now += n;
            ll us = now;
            while(us)
            {
                if(!vis[us % 10])
                    vis[us % 10] = 1,sum++;
                us /= 10;
            }
        }
        if(sum == 10)
            cout << cnt * n << endl;
        else
            cout << "INSOMNIA" << endl;
    }
    return 0;
}