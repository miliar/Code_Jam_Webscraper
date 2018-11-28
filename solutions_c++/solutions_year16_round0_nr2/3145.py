#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>

using namespace std;

char change(char c)
{
    if(c == '+') return '-';
    return '+';
}
int solved(string s)
{
    int ans = 0;
    int len = s.length();
    for(int i = len - 1;i > 0;i --)
    {
        if(s[i] == '+') continue;
        ans ++;
        if(s[0] == '+')
        {
            for(int j = 0;j < i;j ++)
            {
                if(s[j] == '-') break;
                s[j] = '-';
            }
            ans ++;
        }
        for(int j = 0;j <= i / 2;j ++)
        {
            swap(s[j],s[i - j]);
            s[j] = change(s[j]);
            if(j != i - j)
            s[i - j] = change(s[i - j]);
        }

        //cout<<"s = "<<s<<endl;
    }
    if(s[0] == '-')
        ans ++;
    return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    string s;
    cin>>T;
    for(int cas = 1;cas <= T;cas ++)
    {
        cin>>s;
        cout<<"Case #"<<cas<<": "<<solved(s)<<endl;
    }
    return 0;
}
/*
5
-
-+
+-
+++
--+-

+++-------
*/
