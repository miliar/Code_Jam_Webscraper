#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int ary[10020], vis[100020];

int brute_asc(int *st, int len)
{
    if(len == 0 || len == 1)
        return 0;
    int m = 0;
    for(int i = 1; i < len; ++i)
    {
        if(st[i] > st[m])
            m = i;
    }
    //swap
    int ans = 0;
    for(int i = m; i < len -1; ++i)
    {
        swap(st[i], st[i + 1]);
        ans++;
    }
    return ans + brute_asc(st, len - 1);
}

int brute_dsc(int *st, int len)
{
    if(len == 0 || len == 1)
        return 0;
    int m = 0;
    for(int i = 1; i < len; ++i)
    {
        if(st[i] > st[m])
            m = i;
    }
    //swap
    int ans = 0;
    for(int i = m; i > 0; --i)
    {
        swap(st[i], st[i - 1]);
        ans++;
    }
    return ans + brute_dsc(st + 1, len - 1);
}
int min_ans;
void dfs(int *st, int len, int le, int ri, int lans, int op)
{
    if(le == ri)
    {
        if(lans < min_ans)
            min_ans = lans;
        return;
    }
    if(le > ri)
    {
        cout<<"error: le > ri"<<endl;
    }
    if(min_ans <= lans) return;
    if(op & 1)
    {
        int tans = 0;
        for(int i = le; i >= 0; --i)
            if(st[i] > st[i + 1])
            {
                swap(st[i], st[i + 1]);
                ++tans;
            }
        ++le;
        while(le + 1 < len && st[le + 1] > st[le])
            ++le;
        dfs(st, len, le, ri, lans + tans, op>>1);
    }
    else
    {
        int tans = 0;
        for(int i = ri; i < len; ++i)
            if(st[i] > st[i - 1])
            {
                swap(st[i], st[i - 1]);
                ++tans;
            }
        --ri;
        while(ri > 0 && st[ri - 1] > st[ri])
            --ri;
        dfs(st, len, le, ri, lans + tans, op>>1);
    }
}
int mydfs(int *ary, int len)
{
    if(len <= 2)
        return 0;
    int m = 0;
    for(int i = 0; i < len; ++i)
    {
        if(ary[i] < ary[m])
            m = i;
    }
    if(m < len - 1 - m)
    {
        for(int i = m; i > 0; --i)
            swap(ary[i], ary[i - 1]);
        return mydfs(ary + 1, len - 1) + m;
    }
    else
    {
        for(int i = m; i < len - 1; ++i)
            swap(ary[i], ary[i + 1]);
        return mydfs(ary, len - 1) + len - 1 - m;
    }
}

int main()
{
    freopen("2a.in", "r", stdin);
    freopen("2a.out",  "w", stdout);
    int T, n, x;
    cin>>T;
    for(int tt = 1; tt <= T; ++tt)
    {
        cin>>n;
        for(int i = 0; i <n; ++i)
            cin>>ary[i];
        memcpy(vis, ary, sizeof(int) * n);
        /*
        int m = 0;
        for(int i = 1; i < n; ++i)
        {
            if(ary[i] > ary[m])
                m = i;
        }*/
        //int ans = brute_asc(ary, m) + brute_dsc(ary + m + 1, n - m - 1);
        /*min_ans = n * n;
        int le = 0, ri = n - 1;
        while(le < n - 1 && vis[le] < vis[le + 1])
            ++le;
        while(ri > 0 && vis[ri - 1] > vis[ri])
            --ri;

        for(int s = 0; s < (1 << n); ++s)
        {
            memcpy(ary, vis, sizeof(int) * n);
            dfs(ary, n, le, ri, 0, s);
        }*/
        min_ans = mydfs(ary, n);
        cout<<"Case #"<<tt<<": "<<min_ans<<endl;
    }
    return 0;
}
