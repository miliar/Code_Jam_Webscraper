#include <iostream>
#include <queue>
#include <cstdio>
#include <algorithm>

using namespace std;

#define N 1005

int arr[N];
int n;
//priority_queue<int> pq;

int main() {
    int test;
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);
    
    scanf("%d", &test);
    
    for (int cas = 1; cas <= test; cas++) {
        scanf("%d", &n);
        
        int ma = 0;
        
        for (int i = 1; i <= n; i++) {
                scanf("%d", arr + i);
                ma = max(ma, arr[i]);
        }
        
        int res = ma;
        
        for (int i = ma; i >= 1; i--) {
                int cnt = 0;
                for (int j = 1; j <= n; j++) {
                                int v = arr[j];
                                if (v > i) {
                                     cnt += v / i;
                                     if (v % i) cnt++; 
                                     cnt--;                                                                                               
                                }
                }
                
                res = min(res, i + cnt);
        }
        
        printf("Case #%d: %d\n", cas, res);
    }
    
    //while (1);
    return 0;
}
