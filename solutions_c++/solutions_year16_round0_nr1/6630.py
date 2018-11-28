#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

bool solve()
{
    ll k;
    scanf("%lld", &k);
    if (!k) {
        puts("INSOMNIA");
        return false;
    }
    vector<bool> used(10,0);
    int cnt = 0,i;
    for (i = 1; cnt < 10; ++i) {
        ll x = k * i;
        while (x) {
            int o = x%10;
            x/=10;
            cnt += !used[o];
            used[o] = 1;
        }
    }
    printf("%lld\n", k * (i-1));
    return false;
}

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
