#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

int save[2000];
int uni[2000];
int sz;
int sum[2000];
int flec[2000];

inline int cmin (int a, int b)
{
    return a < b ? a : b;
}

int solve (int up)
{
    int res = 0;
    int tmp = up;
    int cur = 0;
    while (true)
    {
        cur = upper_bound(uni,uni+sz,tmp) - uni;
        if (cur >= sz)
            break;
        res += sum[cur];
        tmp += up;
    }
    return res + up;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    std::ios::sync_with_stdio(false);
    int t;
    cin >> t;
    int cas = 0;
    while (cas ++ < t)
    {
        int d;
        cin >> d;
        int i;
        for (i = 0; i < d; i++)
        {
            cin >> save[i];
            uni[i] = save[i];
        }
        sort(save,save+d);
        sort(uni,uni+d);
        sz = unique(uni,uni+d) - uni;
        for (i = 0; i < sz; i++)
        {
            flec[uni[i]] = i;
        }
        memset(sum,0,sizeof(sum));
        for (i = d-1; i>= 0; i--)
        {
            sum[flec[save[i]]] ++;
        }
        for (i = sz-1; i >= 0; i--)
        {
            sum[i] = sum[i+1]+sum[i];
        }
        int res = uni[sz-1];
        for (i = 1; i < uni[sz-1]; i++)
        {
            res = cmin (res,solve(i));
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
