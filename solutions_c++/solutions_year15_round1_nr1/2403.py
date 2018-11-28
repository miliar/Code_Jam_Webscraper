#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
#define all(x) x.begin(), x.end()
typedef long long lng;
const int MOD = 10000007;
const double PI = 3.1415926;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, N;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf("%d", &N);
        int arr[N], y = 0, z = 0, mxd = 0;
        for(int i = 0; i < N; ++i)
        {
            scanf("%d", &arr[i]);
        }
        for(int i = 1; i < N; ++i)
        {
            if(arr[i] < arr[i - 1])
            {
                y += (arr[i - 1] - arr[i]);
                mxd = max(mxd, (arr[i-1] - arr[i]));
            }
        }
        for(int i = 0; i < N - 1; ++i)
        {
            if(arr[i] <= mxd)
            {
                z += arr[i];
            }
            else
            {
                z += mxd;
            }
        }
        printf("%d %d\n", y, z);
    }
    return 0;
}
