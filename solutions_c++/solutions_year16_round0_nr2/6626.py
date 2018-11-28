#include <bits/stdc++.h>

using namespace std;

bool isAllOne(vector<bool> v)
{
    for (int i = 0; i < (int)v.size(); i++)
    {
        if (!v[i]) return false;
    }
    return true;
}

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        printf("Case #%d: ", nc);
        char kode[15];
        scanf("%s", kode);
        vector<bool> t;
        for (int i = 0, len = strlen(kode); i < len; i++)
        {
            t.push_back(kode[i] == '+');
        }
        queue<pair<pair<int, bool>, vector<bool> > > q;
        q.push(make_pair(make_pair(0, false), t));
        int res = 0;
        while (!q.empty())
        {
            auto now = q.front(); q.pop();
            int mov = now.first.first;
            bool last = now.first.second;
            vector<bool> arr = now.second;
            if (isAllOne(arr))
            {
                res = mov;
                while (!q.empty()) q.pop();
                continue;
            }
            bool st = arr[0];
            vector<bool> arr1(arr);
            int i = 0;
            while (arr1[i] == st) { arr1[i] = arr1[i] ^ true; i++; }
            q.push(make_pair(make_pair(mov + 1, false), arr1));
            if (!last)
            {
                vector<bool> arr2(arr.rbegin(), arr.rend());
                arr2.flip();
                q.push(make_pair(make_pair(mov + 1, true), arr2));
            }
        }
        printf("%d\n", res);
    }
}
