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
lng arr[1000010];
lng rev(lng n)
{
    lng r = 0;
    while(n)
    {
        r = r * 10 + (n%10);
        n /= 10;
    }
    return r;
}
int main()
{
    freopen("A-small-attempt6.in", "r", stdin);
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    memset(arr, 0, sizeof(arr));
    arr[1] = 1;
    for(int i = 1; i <= 1000000; ++i)
    {
        if(i%10 == 0)
        {
            arr[i] = arr[i-1] + 1;
            continue;
        }
        lng re = rev(i);
        if(re < i)
        {
            arr[i] = min(arr[re] + 1, arr[i-1] + 1);
        }
        else
        {
            arr[i] = arr[i-1] + 1;
        }
    }
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        lng n, cnt = 1, s = 1;
        cin >> n;
        cout << arr[n] << endl;
    }
    return 0;
}
