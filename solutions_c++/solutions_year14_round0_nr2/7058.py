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

int main()
{
    //freopen("my.out", "w", stdout);
    int T;
    cin >> T;
    for (int kase = 1; kase <= T; kase++)
    {
        double c, f, x;
        cin >> c >> f >> x;
        double ans = 1e9;
        double s = 0;
        int i = 0;
        while (true)
        {
            if (i != 0) s += c * 1.0 / (2 + (i - 1) * f);
            double tmp = s + x / (2 + i * f);
            if (tmp > ans) break;
            if (tmp < ans) ans = tmp;
            i++;
        }
        printf("Case #%d: %.7f\n", kase, ans);
    }
    //fclose(stdout);
}
