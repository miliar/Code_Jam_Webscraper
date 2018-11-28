#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

vector< int > t;
vector< bool > used;

void solve(int test_num)
{
    int n, x;
    scanf("%d %d", &n, &x);
    used.assign(n, false);
    int ans = 0;
    t.resize(n);
    for (int i = 0; i < n; i++)
        scanf("%d", &t[i]);
    
    sort(t.rbegin(), t.rend());
    
    for (int i = 0; i < n; i++) {
        if (used[i])
            continue;
        ans++;
        int ost = x - t[i];
        used[i] = true;
        for (int j = i + 1; j < n; j++) {
            if (!used[j] && t[j] <= ost) {
                used[j] = true;
                break;
            }
        }
    }
    
    printf("Case #%d: %d\n", test_num + 1, ans);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i);
}