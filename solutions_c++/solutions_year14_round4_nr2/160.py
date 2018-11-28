#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

using namespace std;

int T;
int n;
int a[10000];
int order;
bool v[10000];

int solve()
{
    int ans = 0;
    for (int i=0; i<n; ++i) {
        v[i] = true;
    }
    for (int i=0; i<n; ++i) {
        int cnt = 0;
        int minpos = -1;

        for (int j=0; j<n; ++j) {
            if (v[j] && (minpos == -1 || a[minpos] > a[j])) {
                minpos = j;
            }
        }
        int left = 0;
        int right = 0;
        for (int j=0; j<n; ++j) {
            if (!v[j]) continue;
            if (j < minpos) left++;
            if (j > minpos) right++;
        }
        ans += (left < right ? left : right);
        v[minpos] = false;
    }
    return ans;// [)
}

int main()
{
    cin >> T;
    for (int t=1; t<=T; ++t) {
        cin >> n;
        for (int i=0; i<n; ++i) {
            cin >> a[i];
        }
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
