#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

vector< int > a;

void solve(int test_num)
{
    int n;
    scanf("%d", &n);
    a.resize(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    
    if (n <= 2) {
        printf("Case #%d: 0\n", test_num + 1);
        return;
    }
    
    int ans = 0;

    int l = 0, r = n - 1;
    while (l <= r) {
        int min_pos = l;
        for (int i = l + 1; i <= r; i++)
            if (a[i] < a[min_pos]) {
                min_pos = i;
            }
        
        if (min_pos - l < r - min_pos) {
            for (int i = min_pos; i > l; i--) {
                ans++;
                swap(a[i], a[i - 1]);
            }
            l++;
        } else {
            for (int i = min_pos; i < r; i++)
            {
                ans++;
                swap(a[i], a[i + 1]);
            }
            r--;
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