#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
#define LL long long
#define Lowbit(x) ((x)&(-x))
#define lson l, mid, rt << 1
#define rson mid + 1, r, rt << 1|1
#define MP(a, b) make_pair(a, b)
const int INF = 0x3f3f3f3f;
const int Mod = 1000000007;
const int maxn = 12;
const double eps = 1e-8;
const double PI = acos(-1.0);
set<int> s;

void getnum(int n)
{
    while (n > 0)
    {
        s.insert(n % 10);
        n /= 10;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for (int ncase = 1; ncase <= T; ncase++)
    {
        int n;
        cin >> n;
        cout << "Case #" << ncase << ": ";
        if (n == 0) cout << "INSOMNIA" << endl;
        else
        {
            int k = 1;
            s.clear();
            while (s.size() != 10)
            {
                getnum(k*n);
                k++;
            }
            cout << n * (k - 1) << endl;
        }
    }
    return 0;
}
