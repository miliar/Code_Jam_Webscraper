#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> gen(int winner, int round)
{
    vector<int> cur;
    cur.push_back(winner);
    for (int i = 0; i < round; i++)
    {
        vector<int> pre;
        pre.swap(cur);
        for (int j = 0; j < (int)pre.size(); j++)
        {
            switch (pre[j])
            {
            case 0:
                cur.push_back(0);
                cur.push_back(1);
                break;
            case 1:
                cur.push_back(1);
                cur.push_back(2);
                break;
            default:
                cur.push_back(0);
                cur.push_back(2);
                break;
            }
        }
    }
    return cur;
}

char ch[3] = {'P', 'R', 'S'};

void resort(vector<int> &arr, int s, int t)
{
    if (s >= t) return;
    int mid = (s + t) >> 1, flag = 0;
    for (int i = s, j = mid + 1; i <= mid; i++, j++)
    {
        if (arr[i] < arr[j]) break;
        if (arr[i] > arr[j])
        {
            flag = 1;
            break;
        }
    }
    if (flag)
    {
        for (int i = s, j = mid + 1; i <= mid; i++, j++)
            swap(arr[i], arr[j]);
    }
    resort(arr, s, mid);
    resort(arr, mid + 1, t);
}

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int N, R, P, S, flag = 0;
        scanf("%d%d%d%d", &N, &R, &P, &S);
        printf("Case #%d: ", cas);
        for (int i = 0; i < 3; i++)
        {
            vector<int> arr;
            arr = gen(i, N);
            int num[3];
            for (int j = 0; j < 3; j++) num[j] = 0;
            for (int j = 0; j < (int)arr.size(); j++)
            {
                num[arr[j]] += 1;
            }
            if (num[0] != P) continue;
            if (num[1] != R) continue;
            if (num[2] != S) continue;
            resort(arr, 0, (int)arr.size() - 1);
            for (int j = 0; j < (int)arr.size(); j++)
                printf("%c", ch[arr[j]]);
            puts("");
            flag = 1;
            break;
        }
        if (!flag) puts("IMPOSSIBLE");
    }
    return 0;
}
