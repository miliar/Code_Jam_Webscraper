#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <sstream>
#include <cstring>
#include <vector>
#include <map>
#include <set>
using namespace std;

const int maxn = 10000;
int a[maxn];
int n;

int main() {    
    int T;
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", a + i);
        
        int le = 0, ri = n - 1;
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            int min_ind = le;
            for (int j = le + 1; j <= ri; j++)
                if (a[j] < a[min_ind])
                    min_ind = j;
            if (abs(min_ind - le) < abs(min_ind -ri)) {
                ans += abs(min_ind - le);
                for (int j = min_ind; j > le; j--)
                    swap(a[j], a[j - 1]);
                le++;
            } else {
                ans += abs(min_ind - ri);
                for (int j = min_ind; j < ri; j++)
                    swap(a[j], a[j + 1]);
                ri--;
            }
        }
        
        printf("Case #%d: %d", t, ans);
        
        printf("\n");
    }
}

