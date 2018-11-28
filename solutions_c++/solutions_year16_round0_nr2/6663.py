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
#define sp system("pause")
#define complete_unique(x) x.erase(unique(x.begin(),x.end()),x.end())
using namespace std;
typedef long long ll;

string s;

bool check()
{
    int i;
    for(i = s.size() - 1;i >= 0;i--)
    {
        if(s[i] == '-')
        {
            break;
        }
    }
    if(i == -1)
        return false;
    if(s[0] == '+')
    {
        for(int j = 0;j < s.size();j++)
        {
            if(s[j] == '-')
            {
                for(int k = 0;k < j;k++)
                    s[k] = '-';
                return true;
            }
        }
    }
    reverse(s.begin(),s.begin() + i + 1);

    //cout << i << endl;sp;
    for(int j = 0;j <= i;j++)
    {
        if(s[j] == '-')
            s[j] = '+';
        else
            s[j] = '-';
    }
    return true;
}


int main()
{
    //freopen("B-large.in","r",stdin);
   //  freopen("B-large.out","w",stdout);
    int t,cas = 1;
    cin >> t;
    while(t--)
    {
        int cnt = 0;
        cin >> s;
        printf("Case #%d: ",cas++);
        while(check())
        {
          //  cout << s << endl;sp;
            cnt++;
        }
        cout << cnt << endl;
    }
    return 0;
}