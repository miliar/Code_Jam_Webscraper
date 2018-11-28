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
    freopen("/Users/lujcmss/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/output.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int kase = 0; kase < T; kase++) {
        int n;
        cin >> n;
        
        printf("Case #%d: ", kase+1);
        if (n == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        
        unordered_map<int, int> m;
        m.clear();
        
        int cur = 0;
        while (m.size() < 10) {
            cur += n;
            int x = cur;
            while (x > 0) {
                m[x%10] = 1;
                x /= 10;
            }
        }
        printf("%d\n", cur);
    }
    
    return 0;
}