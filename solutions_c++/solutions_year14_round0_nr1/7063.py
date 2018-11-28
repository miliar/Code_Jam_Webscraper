#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <cstdlib>
#include <ctime>
using namespace std;

#pragma comment(linker,"/STACK:102400000,102400000")

#define LL long long
#define ULL unsigned long long
#define Hei cout << "Czy!!!" << endl;
#define lson rt << 1, l, mid
#define rson  rt << 1 | 1, mid + 1, r
#define MOD 1000000007
#define maxn 210
#define INF 0x3f3f3f3f

/*
clock_t t1, t2;
t1 = clock();
t2 = clock();
cout << (double)(t2 - t1) / CLOCKS_PER_SEC << endl;
*/

int cnt[110];

int main()
{
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; kase++)
    {
        memset(cnt, 0, sizeof(cnt));
        int n;
        cin >> n;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
            {
                int x;
                scanf("%d", &x);
                if (i == n) cnt[x]++;
            }
        cin >> n;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++)
            {
                int x;
                scanf("%d", &x);
                if (i == n) cnt[x]++;
            }
        int ans = 0, id;
        for (int i = 1; i <= 16; i++)
            if (cnt[i] == 2)
            {
                id = i;
                ans++;
            }
        cout << "Case #" << kase << ": ";
        if (ans == 1) cout << id << endl;
        if (ans == 0) puts("Volunteer cheated!");
        if (ans > 1) puts("Bad magician!");
    }
}
