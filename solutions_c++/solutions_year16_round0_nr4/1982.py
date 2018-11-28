#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>
#include <time.h>
#include <errno.h>
#include <Semaphore.h>

using namespace std;

int main() {
    freopen("/Users/lujcmss/Downloads/D-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int kase = 0; kase < T; kase++) {
        int k, c, s;
        cin >> k >> c >> s;
        if (c > k) {
            c = k;
        }
        
        printf("Case #%d:", kase+1);
        
        if ((k - 1) / c + 1 > s) {
            printf(" IMPOSSIBLE\n");
            continue;
        }
        
        for (int i = 0; i < (k - 1) / c + 1; i++) {
            long long ans = 0;
            long long base = 1;
            long long pos = i * c;
            for (int j = 0; j < c; j++) {
                if (pos == k) {
                    break;
                }
                ans += base * pos;
                base *= k;
                pos++;
            }
            printf(" %lld", ans+1);
        }
        printf("\n");
    }
    
    return 0;
}