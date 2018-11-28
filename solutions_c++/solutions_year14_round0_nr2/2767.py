#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cmath>
using namespace std;
const int mod = 1000000007;
typedef long long LL;

int a[5][5];
bool vis[20];

int main()
{
    int T, nc = 0;
    cin >> T;
    while(T--)
    {
        printf("Case #%d: ", ++nc);
        double C, F, X, ans;
        int N;

        cin >> C >> F >> X;
        N = (int)(ceil((F*X/C-2) / F) + 0.1);
        N = max(N, 1);
        ans = X/(2+(N-1)*F);
        for(int i = 0; i < N-1; i++)
            ans += C / (2 + i*F);

        printf("%.7f\n", ans);
    }
    return 0;
}
